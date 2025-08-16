#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MSB Scraper Email Bildirim Sistemi
Yeni temin ve duyuru geldikçe otomatik email atar
"""

import json
import smtplib
import os
import hashlib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
import time
import re

class MSBEmailNotifier:
    def __init__(self, config_file='email_config.json'):
        self.config_file = config_file
        self.data_file = 'data/msb_data.json'
        self.history_file = 'data/email_history.json'
        self.config = self.load_config()
        self.history = self.load_history()
        
    def load_config(self):
        """Email konfigürasyonunu yükle"""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # Varsayılan konfigürasyon
            default_config = {
                "smtp_server": "smtp.gmail.com",
                "smtp_port": 587,
                "sender_email": "your_email@gmail.com",
                "sender_password": "your_app_password",
                "recipients": ["recipient1@example.com", "recipient2@example.com"],
                "check_interval": 3600,  # 1 saat (saniye)
                "max_items_per_email": 10,
                "email_subject_prefix": "🚀 MSB Scraper - Yeni ",
                "include_old_items": False,
                "old_items_days": 7
            }
            
            # Konfigürasyon dosyasını oluştur
            self.save_config(default_config)
            print(f"⚠️  Varsayılan konfigürasyon oluşturuldu: {self.config_file}")
            print("📧 Lütfen email ayarlarını düzenleyin!")
            return default_config
    
    def save_config(self, config):
        """Konfigürasyonu kaydet"""
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
    
    def load_history(self):
        """Email geçmişini yükle"""
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"sent_emails": [], "last_check": None}
    
    def save_history(self):
        """Email geçmişini kaydet"""
        os.makedirs('data', exist_ok=True)
        with open(self.history_file, 'w', encoding='utf-8') as f:
            json.dump(self.history, f, ensure_ascii=False, indent=2)
    
    def get_data_hash(self, data):
        """Veri için hash oluştur"""
        data_str = json.dumps(data, sort_keys=True, ensure_ascii=False)
        return hashlib.md5(data_str.encode()).hexdigest()
    
    def parse_date(self, date_str):
        """Farklı tarih formatlarını parse et"""
        if not date_str:
            return None
            
        # ISO format (2024-12-15T10:30:00)
        try:
            return datetime.fromisoformat(date_str)
        except ValueError:
            pass
        
        # Türkçe format (15.12.2024)
        try:
            if re.match(r'\d{2}\.\d{2}\.\d{4}', date_str):
                return datetime.strptime(date_str, '%d.%m.%Y')
        except ValueError:
            pass
        
        # Türkçe format (15.12.2024 10:30)
        try:
            if re.match(r'\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}', date_str):
                return datetime.strptime(date_str, '%d.%m.%Y %H:%M')
        except ValueError:
            pass
        
        # Türkçe format (15.12.2024 10:30:00)
        try:
            if re.match(r'\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}', date_str):
                return datetime.strptime(date_str, '%d.%m.%Y %H:%M:%S')
        except ValueError:
            pass
        
        # Standart format (15/12/2024)
        try:
            if re.match(r'\d{2}/\d{2}/\d{4}', date_str):
                return datetime.strptime(date_str, '%d/%m/%Y')
        except ValueError:
            pass
        
        # YYYY-MM-DD format
        try:
            if re.match(r'\d{4}-\d{2}-\d{2}', date_str):
                return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            pass
        
        print(f"⚠️  Tarih formatı tanınamadı: {date_str}")
        return None
    
    def check_for_new_items(self):
        """Yeni öğeleri kontrol et"""
        if not os.path.exists(self.data_file):
            print("❌ Veri dosyası bulunamadı!")
            return None, None
        
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                current_data = json.load(f)
            
            current_hash = self.get_data_hash(current_data)
            last_hash = self.history.get('last_data_hash')
            
            if current_hash == last_hash:
                print("✅ Yeni veri yok")
                return None, None
            
            # Hash'i güncelle
            self.history['last_data_hash'] = current_hash
            
            # Yeni öğeleri bul
            new_teminler = []
            new_duyurular = []
            
            # Son email gönderim zamanını al
            last_email_time = self.history.get('last_check')
            if last_email_time:
                last_email_time = datetime.fromisoformat(last_email_time)
            else:
                last_email_time = datetime.now() - timedelta(days=1)
            
            # Teminler
            if 'guncel_teminler' in current_data:
                for temin in current_data['guncel_teminler']:
                    temin_time = self.parse_date(temin.get('tarih'))
                    if temin_time and temin_time > last_email_time:
                        new_teminler.append(temin)
            
            # Duyurular
            if 'guncel_duyurular' in current_data:
                for duyuru in current_data['guncel_duyurular']:
                    duyuru_time = self.parse_date(duyuru.get('tarih'))
                    if duyuru_time and duyuru_time > last_email_time:
                        new_duyurular.append(duyuru)
            
            return new_teminler, new_duyurular
            
        except Exception as e:
            print(f"❌ Veri kontrol hatası: {e}")
            return None, None
    
    def create_email_content(self, new_teminler, new_duyurular):
        """Email içeriğini oluştur"""
        subject = f"{self.config['email_subject_prefix']}"
        if new_teminler and new_duyurular:
            subject += "Temin ve Duyuru"
        elif new_teminler:
            subject += "Temin"
        elif new_duyurular:
            subject += "Duyuru"
        else:
            subject += "Güncelleme"
        
        # HTML içerik
        html_content = f"""
        <!DOCTYPE html>
        <html lang="tr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>MSB Scraper - Yeni Güncellemeler</title>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                .container {{ max-width: 800px; margin: 0 auto; padding: 20px; }}
                .header {{ background: #2c3e50; color: white; padding: 20px; border-radius: 10px; text-align: center; }}
                .section {{ margin: 20px 0; padding: 15px; border-left: 4px solid #3498db; background: #f8f9fa; }}
                .item {{ background: white; padding: 15px; margin: 10px 0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
                .title {{ font-weight: bold; color: #2c3e50; margin-bottom: 8px; }}
                .description {{ color: #7f8c8d; margin-bottom: 8px; }}
                .date {{ color: #95a5a6; font-size: 0.9em; }}
                .link {{ color: #3498db; text-decoration: none; }}
                .footer {{ text-align: center; margin-top: 30px; color: #7f8c8d; font-size: 0.9em; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>🚀 MSB Scraper</h1>
                    <p>Yeni Güncellemeler - {datetime.now().strftime('%d.%m.%Y %H:%M')}</p>
                </div>
        """
        
        if new_teminler:
            html_content += f"""
                <div class="section">
                    <h2>📋 Yeni Teminler ({len(new_teminler)})</h2>
            """
            
            for temin in new_teminler[:self.config['max_items_per_email']]:
                html_content += f"""
                    <div class="item">
                        <div class="title">{temin.get('başlık', 'Başlık bulunamadı')}</div>
                        <div class="description">{temin.get('açıklama', 'Açıklama bulunamadı')}</div>
                        <div class="date">📅 {temin.get('tarih', 'Tarih bulunamadı')}</div>
                        {f'<div><a href="{temin["link"]}" class="link" target="_blank">🔗 Detayları Görüntüle</a></div>' if temin.get('link') else ''}
                    </div>
                """
            
            html_content += "</div>"
        
        if new_duyurular:
            html_content += f"""
                <div class="section">
                    <h2>📢 Yeni Duyurular ({len(new_duyurular)})</h2>
            """
            
            for duyuru in new_duyurular[:self.config['max_items_per_email']]:
                html_content += f"""
                    <div class="item">
                        <div class="title">{duyuru.get('başlık', 'Başlık bulunamadı')}</div>
                        <div class="description">{duyuru.get('açıklama', 'Açıklama bulunamadı')}</div>
                        <div class="date">📅 {duyuru.get('tarih', 'Tarih bulunamadı')}</div>
                        {f'<div><a href="{duyuru["link"]}" class="link" target="_blank">🔗 Detayları Görüntüle</a></div>' if duyuru.get('link') else ''}
                    </div>
                """
            
            html_content += "</div>"
        
        html_content += f"""
                <div class="footer">
                    <p>Bu email MSB Scraper tarafından otomatik olarak gönderilmiştir.</p>
                    <p>📊 Web Arayüzü: <a href="https://veliozcan0.github.io/pertem/" class="link">https://veliozcan0.github.io/pertem/</a></p>
                    <p>🔗 GitHub: <a href="https://github.com/veliozcan0/pertem" class="link">https://github.com/veliozcan0/pertem</a></p>
                </div>
            </div>
        </body>
        </html>
        """
        
        return subject, html_content
    
    def send_email(self, subject, html_content):
        """Email gönder"""
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = self.config['sender_email']
            msg['To'] = ', '.join(self.config['recipients'])
            
            # HTML içerik ekle
            html_part = MIMEText(html_content, 'html', 'utf-8')
            msg.attach(html_part)
            
            # SMTP bağlantısı
            server = smtplib.SMTP(self.config['smtp_server'], self.config['smtp_port'])
            server.starttls()
            server.login(self.config['sender_email'], self.config['sender_password'])
            
            # Email gönder
            server.send_message(msg)
            server.quit()
            
            print(f"✅ Email başarıyla gönderildi: {subject}")
            return True
            
        except Exception as e:
            print(f"❌ Email gönderme hatası: {e}")
            return False
    
    def run_notification_check(self):
        """Bildirim kontrolünü çalıştır"""
        print(f"🔍 Yeni öğeler kontrol ediliyor... {datetime.now().strftime('%H:%M:%S')}")
        
        new_teminler, new_duyurular = self.check_for_new_items()
        
        if new_teminler or new_duyurular:
            print(f"📧 Yeni öğeler bulundu: {len(new_teminler or [])} temin, {len(new_duyurular or [])} duyuru")
            
            subject, html_content = self.create_email_content(new_teminler, new_duyurular)
            
            if self.send_email(subject, html_content):
                # Geçmişi güncelle
                self.history['last_check'] = datetime.now().isoformat()
                self.history['sent_emails'].append({
                    'timestamp': datetime.now().isoformat(),
                    'subject': subject,
                    'temin_count': len(new_teminler or []),
                    'duyuru_count': len(new_duyurular or [])
                })
                
                # Son 100 email'i tut
                if len(self.history['sent_emails']) > 100:
                    self.history['sent_emails'] = self.history['sent_emails'][-100:]
                
                self.save_history()
        else:
            print("✅ Yeni öğe yok")
    
    def start_monitoring(self):
        """Sürekli izlemeyi başlat"""
        print("🚀 MSB Email Bildirim Sistemi Başlatıldı!")
        print(f"📧 SMTP Server: {self.config['smtp_server']}:{self.config['smtp_port']}")
        print(f"📨 Gönderen: {self.config['sender_email']}")
        print(f"👥 Alıcılar: {', '.join(self.config['recipients'])}")
        print(f"⏰ Kontrol Aralığı: {self.config['check_interval']} saniye")
        print("=" * 60)
        
        try:
            while True:
                self.run_notification_check()
                time.sleep(self.config['check_interval'])
                
        except KeyboardInterrupt:
            print("\n🛑 Sistem durduruldu!")
        except Exception as e:
            print(f"❌ Beklenmeyen hata: {e}")

def main():
    """Ana fonksiyon"""
    notifier = MSBEmailNotifier()
    
    # Konfigürasyon kontrol
    if (notifier.config['sender_email'] == 'your_email@gmail.com' or 
        notifier.config['sender_password'] == 'your_app_password'):
        print("⚠️  Lütfen email konfigürasyonunu düzenleyin!")
        print(f"📝 Dosya: {notifier.config_file}")
        return
    
    # Tek seferlik kontrol
    if len(sys.argv) > 1 and sys.argv[1] == '--check':
        notifier.run_notification_check()
    else:
        # Sürekli izleme
        notifier.start_monitoring()

if __name__ == "__main__":
    import sys
    main()
