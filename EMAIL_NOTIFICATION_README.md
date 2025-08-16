# 📧 MSB Scraper Email Bildirim Sistemi

Yeni temin ve duyuru geldikçe otomatik email atan akıllı bildirim sistemi.

## 🚀 **Özellikler**

### **1. Otomatik Bildirimler:**
- **🔍 Akıllı Kontrol**: Hash tabanlı değişiklik tespiti
- **📧 HTML Email**: Güzel tasarımlı email içeriği
- **⏰ Zamanlı Kontrol**: Belirlenen aralıklarla otomatik kontrol
- **📊 Detaylı Bilgi**: Başlık, açıklama, tarih ve link

### **2. Filtreleme:**
- **🆕 Sadece Yeni**: Son email gönderiminden sonraki öğeler
- **📋 Teminler**: Yeni temin bildirimleri
- **📢 Duyurular**: Yeni duyuru bildirimleri
- **📅 Tarih Bazlı**: Zaman filtreleme

### **3. Konfigürasyon:**
- **📧 SMTP Ayarları**: Gmail, Outlook, vb.
- **👥 Alıcı Listesi**: Birden fazla email adresi
- **⏱️ Kontrol Aralığı**: Özelleştirilebilir süre
- **📝 Email Şablonu**: Özelleştirilebilir içerik

## 📋 **Kurulum**

### **1. Gerekli Dosyalar:**
- `email_notifier.py` - Ana email bildirim script'i
- `email_config.json` - Email konfigürasyonu
- `.github/workflows/daily-scraper.yml` - GitHub Actions workflow

### **2. Gmail Kurulumu (Önerilen):**

#### **A. App Password Oluşturma:**
1. **Google Hesabı** → **Güvenlik**
2. **2 Adımlı Doğrulama** → **Açık**
3. **Uygulama Şifreleri** → **Uygulama Şifresi Oluştur**
4. **Uygulama**: "Mail" seçin
5. **Oluşturulan şifreyi kopyalayın**

#### **B. Konfigürasyon:**
```json
{
  "smtp_server": "smtp.gmail.com",
  "smtp_port": 587,
  "sender_email": "your_email@gmail.com",
  "sender_password": "your_app_password",
  "recipients": ["recipient1@example.com", "recipient2@example.com"]
}
```

### **3. GitHub Secrets Kurulumu:**

#### **A. Repository Secrets:**
1. **Settings** → **Secrets and variables** → **Actions**
2. **New repository secret** ekleyin:

| Secret Name | Value |
|-------------|-------|
| `SMTP_SERVER` | `smtp.gmail.com` |
| `SMTP_PORT` | `587` |
| `SENDER_EMAIL` | `your_email@gmail.com` |
| `SENDER_PASSWORD` | `your_app_password` |
| `RECIPIENTS` | `email1@example.com,email2@example.com` |

#### **B. Secrets Formatı:**
- **RECIPIENTS**: Virgülle ayrılmış email listesi
- **SENDER_PASSWORD**: Gmail App Password (normal şifre değil!)

## 🎯 **Kullanım**

### **1. Manuel Çalıştırma:**
```bash
# Tek seferlik kontrol
python email_notifier.py --check

# Sürekli izleme
python email_notifier.py
```

### **2. GitHub Actions ile:**
- Workflow otomatik olarak email bildirim sistemini çalıştırır
- Veri çekme tamamlandıktan sonra email kontrol edilir
- Yeni öğeler varsa email gönderilir

### **3. Yerel Sunucu ile:**
```bash
# Sürekli izleme (1 saat aralıklarla)
python email_notifier.py

# Özel aralık (30 dakika)
# email_config.json'da "check_interval": 1800
```

## 📧 **Email İçeriği**

### **1. HTML Format:**
- **Responsive tasarım**
- **Modern CSS stilleri**
- **Emoji ve ikonlar**
- **Link'ler ve butonlar**

### **2. İçerik Yapısı:**
```
🚀 MSB Scraper - Yeni Temin ve Duyuru

📋 Yeni Teminler (3)
├── Başlık 1
├── Açıklama 1
├── 📅 15.12.2024
└── 🔗 Detayları Görüntüle

📢 Yeni Duyurular (2)
├── Başlık 1
├── Açıklama 1
├── 📅 15.12.2024
└── 🔗 Detayları Görüntüle

📊 Web Arayüzü: https://veliozcan0.github.io/pertem/
🔗 GitHub: https://github.com/veliozcan0/pertem
```

## ⚙️ **Konfigürasyon Seçenekleri**

### **1. Temel Ayarlar:**
```json
{
  "check_interval": 3600,           // Kontrol aralığı (saniye)
  "max_items_per_email": 10,        // Email başına max öğe
  "email_subject_prefix": "🚀 MSB Scraper - Yeni ",
  "include_old_items": false,       // Eski öğeleri dahil et
  "old_items_days": 7               // Kaç günlük eski öğe
}
```

### **2. SMTP Sunucuları:**

#### **Gmail:**
```json
{
  "smtp_server": "smtp.gmail.com",
  "smtp_port": 587
}
```

#### **Outlook/Hotmail:**
```json
{
  "smtp_server": "smtp-mail.outlook.com",
  "smtp_port": 587
}
```

#### **Yandex:**
```json
{
  "smtp_server": "smtp.yandex.com",
  "smtp_port": 587
}
```

## 🔧 **Gelişmiş Özellikler**

### **1. Hash Tabanlı Kontrol:**
- **MD5 hash** ile veri değişikliği tespiti
- **Gereksiz email** önleme
- **Performans** optimizasyonu

### **2. Email Geçmişi:**
- **Son 100 email** kaydı
- **Gönderim zamanları**
- **Öğe sayıları**

### **3. Hata Yönetimi:**
- **SMTP bağlantı hataları**
- **Veri okuma hataları**
- **Otomatik yeniden deneme**

## 📱 **Mobil Uyumluluk**

### **1. Responsive Email:**
- **Tüm cihazlarda** düzgün görünüm
- **Mobil tarayıcılar** için optimize
- **Touch-friendly** linkler

### **2. Email İstemcileri:**
- **Gmail** (mobil/desktop)
- **Outlook** (mobil/desktop)
- **Apple Mail**
- **Thunderbird**

## 🚨 **Güvenlik**

### **1. App Password:**
- **2FA zorunlu**
- **Normal şifre kullanmayın**
- **Güvenli token yönetimi**

### **2. GitHub Secrets:**
- **Şifreler gizli**
- **Repository'de görünmez**
- **Güvenli erişim**

### **3. SMTP Güvenliği:**
- **TLS/SSL** bağlantı
- **Port 587** (STARTTLS)
- **Güvenli kimlik doğrulama**

## 🔄 **Güncelleme**

### **1. Konfigürasyon Güncelleme:**
```bash
# email_config.json dosyasını düzenleyin
# Script otomatik olarak yeniden yükler
```

### **2. Script Güncelleme:**
```bash
git pull origin main
# Yeni özellikler otomatik olarak aktif olur
```

### **3. GitHub Actions Güncelleme:**
- Workflow otomatik olarak güncellenir
- Yeni email özellikleri eklenir
- Geriye uyumluluk korunur

## 📞 **Destek**

### **1. Yaygın Sorunlar:**

#### **SMTP Hatası:**
```
❌ Email gönderme hatası: Authentication failed
```
**Çözüm**: App Password kullandığınızdan emin olun

#### **Veri Bulunamadı:**
```
❌ Veri dosyası bulunamadı!
```
**Çözüm**: `data/msb_data.json` dosyasının varlığını kontrol edin

#### **Hash Hatası:**
```
❌ Veri kontrol hatası: Invalid date format
```
**Çözüm**: Tarih formatının ISO standardında olduğundan emin olun

### **2. Debug Modu:**
```bash
# Detaylı log için
python email_notifier.py --check --debug
```

### **3. Test Email:**
```bash
# Test email gönderimi
python -c "
from email_notifier import MSBEmailNotifier
notifier = MSBEmailNotifier()
notifier.send_test_email()
"
```

---

**Not**: Email bildirim sistemi, veri çekme işlemi tamamlandıktan sonra otomatik olarak çalışır. Yeni öğeler varsa HTML formatında güzel email'ler gönderir.
