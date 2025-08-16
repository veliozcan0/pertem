#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MSB Personel Temin Scraper - GitHub Actions Versiyonu
Bu script GitHub Actions ortamında çalışmak üzere optimize edilmiştir.
"""

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import os
import sys

def fetch_msb_data():
    """
    MSB Personel Temin sitesinden GÜNCEL TEMİNLER ve GÜNCEL DUYURULAR verilerini çeker
    """
    url = "https://personeltemin.msb.gov.tr"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'tr-TR,tr;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    
    try:
        print("Siteye bağlanılıyor...")
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        # Türkçe karakterleri düzgün parse etmek için encoding ayarla
        response.encoding = 'utf-8'
        
        print("HTML parse ediliyor...")
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # GÜNCEL TEMİNLER bölümünü çek
        print("GÜNCEL TEMİNLER verileri çekiliyor...")
        teminler_data = []
        
        # GÜNCEL TEMİNLER tab'ını bul
        teminler_tab = soup.find('div', class_='tab-item active')
        if teminler_tab and 'GÜNCEL TEMİNLER' in teminler_tab.get_text():
            # Teminler içeriğini bul
            teminler_content = soup.find('div', class_='tab-border-left')
            if teminler_content:
                teminler_items = teminler_content.find_all('div', class_='item cal')
                
                for item in teminler_items:
                    try:
                        # Başlık
                        title_elem = item.find('h3')
                        title = title_elem.get_text(strip=True) if title_elem else "Başlık bulunamadı"
                        
                        # Açıklama - h3'ten sonraki ilk p elementi
                        desc_elem = title_elem.find_next_sibling('p') if title_elem else None
                        description = desc_elem.get_text(strip=True) if desc_elem else "Açıklama bulunamadı"
                        
                        # Tarih
                        date_elem = item.find('p', class_='date')
                        date = date_elem.get_text(strip=True) if date_elem else "Tarih bulunamadı"
                        
                        # Link
                        onclick_attr = item.get('onclick', '')
                        link = None
                        if 'window.location.href=' in onclick_attr:
                            link_start = onclick_attr.find("'") + 1
                            link_end = onclick_attr.find("'", link_start)
                            if link_start > 0 and link_end > link_start:
                                link = url + onclick_attr[link_start:link_end]
                        
                        teminler_data.append({
                            'başlık': title,
                            'açıklama': description,
                            'tarih': date,
                            'link': link
                        })
                        
                    except Exception as e:
                        print(f"Temin verisi parse edilirken hata: {e}")
                        continue
        
        # GÜNCEL DUYURULAR bölümünü çek
        print("GÜNCEL DUYURULAR verileri çekiliyor...")
        duyurular_data = []
        
        # Sağ taraftaki duyurular bölümünü bul
        duyurular_content = soup.find('div', class_='tab-border-right')
        if duyurular_content:
            duyurular_items = duyurular_content.find_all('div', class_='item cal')
            
            for item in duyurular_items:
                try:
                    # Takvim bilgisi
                    cal_elem = item.find('div', class_='item--cal')
                    month = ""
                    day = ""
                    weekday = ""
                    
                    if cal_elem:
                        month_elem = cal_elem.find('p', class_='top-line')
                        if month_elem:
                            month = month_elem.get_text(strip=True)
                        
                        date_elem = cal_elem.find('p', class_='date')
                        if date_elem:
                            day = date_elem.get_text(strip=True)
                        
                        weekday_elem = cal_elem.find('p', class_='day')
                        if weekday_elem:
                            weekday = weekday_elem.get_text(strip=True)
                    
                    # Duyuru bilgisi
                    exp_elem = item.find('div', class_='item--exp')
                    title = ""
                    date = ""
                    
                    if exp_elem:
                        title_elem = exp_elem.find('h3')
                        if title_elem:
                            title = title_elem.get_text(strip=True)
                        
                        date_elem = exp_elem.find('p', class_='date')
                        if date_elem:
                            date = date_elem.get_text(strip=True)
                    
                    # Link
                    onclick_attr = item.get('onclick', '')
                    link = None
                    if 'window.location.href' in onclick_attr:
                        link_start = onclick_attr.find("'") + 1
                        link_end = onclick_attr.find("'", link_start)
                        if link_start > 0 and link_end > link_start:
                            link = url + onclick_attr[link_start:link_end]
                    
                    duyurular_data.append({
                        'ay': month,
                        'gün': day,
                        'gün_adı': weekday,
                        'başlık': title,
                        'tarih': date,
                        'link': link
                    })
                    
                except Exception as e:
                    print(f"Duyuru verisi parse edilirken hata: {e}")
                    continue
        
        return {
            'guncel_teminler': teminler_data,
            'guncel_duyurular': duyurular_data,
            'çekim_tarihi': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    
    except requests.exceptions.RequestException as e:
        print(f"Bağlantı hatası: {e}")
        return None
    except Exception as e:
        print(f"Genel hata: {e}")
        return None

def save_to_json(data, filename='msb_data.json'):
    """
    Verileri JSON dosyasına kaydeder
    """
    try:
        # Veri klasörünü oluştur
        os.makedirs('data', exist_ok=True)
        
        # Tam dosya yolu
        filepath = os.path.join('data', filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Veriler {filepath} dosyasına kaydedildi.")
        
        # Tarihli yedek dosya da oluştur
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_filename = f'msb_data_{timestamp}.json'
        backup_filepath = os.path.join('data', backup_filename)
        
        with open(backup_filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Yedek dosya {backup_filepath} oluşturuldu.")
        
    except Exception as e:
        print(f"Dosya kaydedilirken hata: {e}")
        sys.exit(1)

def main():
    """
    Ana fonksiyon - GitHub Actions için optimize edilmiş
    """
    print("MSB Personel Temin Sitesi Veri Çekme Aracı - GitHub Actions")
    print("=" * 60)
    
    # Veriyi çek
    data = fetch_msb_data()
    
    if data:
        # JSON dosyasına kaydet
        save_to_json(data)
        
        print(f"\n✅ Başarılı! Toplam {len(data.get('guncel_teminler', []))} temin ve {len(data.get('guncel_duyurular', []))} duyuru bulundu.")
        print(f"📅 Çekim Tarihi: {data.get('çekim_tarihi', 'Bilinmiyor')}")
        
        # GitHub Actions için exit code
        sys.exit(0)
    else:
        print("❌ Veri çekilemedi!")
        sys.exit(1)

if __name__ == "__main__":
    main()
