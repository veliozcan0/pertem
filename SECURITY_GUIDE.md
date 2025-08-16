# 🔒 MSB Scraper Güvenlik Rehberi

Email bildirim sistemi için güvenlik önlemleri ve best practices.

## 🚨 **Güvenlik Uyarıları**

### **1. Email Konfigürasyonu:**
- **❌ HİÇBİR ZAMAN** `email_config.json` dosyasını GitHub'a yüklemeyin
- **❌ HİÇBİR ZAMAN** email şifrelerini public repository'de paylaşmayın
- **❌ HİÇBİR ZAMAN** App Password'leri kod içinde tutmayın

### **2. Dosya Güvenliği:**
- `email_config.json` → `.gitignore` ile korunur
- `email_history.json` → `.gitignore` ile korunur
- Hassas bilgiler → GitHub Secrets ile saklanır

## 📋 **Güvenli Kurulum Adımları**

### **1. Yerel Konfigürasyon:**
```bash
# 1. Template'i kopyalayın
cp email_config_template.json email_config.json

# 2. Kendi bilgilerinizle düzenleyin
# 3. Dosyayı test edin
python email_notifier.py --check
```

### **2. GitHub Secrets Kurulumu:**
1. **Repository Settings** → **Secrets and variables** → **Actions**
2. **New repository secret** ekleyin:

| Secret Name | Value | Açıklama |
|-------------|-------|----------|
| `SMTP_SERVER` | `smtp.gmail.com` | SMTP sunucu adresi |
| `SMTP_PORT` | `587` | SMTP port numarası |
| `SENDER_EMAIL` | `your_email@gmail.com` | Gönderen email |
| `SENDER_PASSWORD` | `your_app_password` | Gmail App Password |
| `RECIPIENTS` | `email1@example.com,email2@example.com` | Alıcı listesi |

### **3. .gitignore Kontrolü:**
```bash
# .gitignore dosyasında şu satırlar olmalı:
email_config.json
email_history.json
```

## 🔐 **Gmail App Password Güvenliği**

### **1. 2FA Zorunlu:**
- **Google Hesabı** → **Güvenlik**
- **2 Adımlı Doğrulama** → **Açık**
- **Uygulama Şifreleri** → **Mail** seçin

### **2. App Password Oluşturma:**
1. **Güvenlik** → **2 Adımlı Doğrulama**
2. **Uygulama Şifreleri** → **Uygulama Şifresi Oluştur**
3. **Uygulama**: "Mail" seçin
4. **Oluşturulan şifreyi kopyalayın**

### **3. Güvenlik Kuralları:**
- **Normal şifre kullanmayın**
- **App Password'ü güvenli saklayın**
- **Düzenli olarak yenileyin**
- **Şüpheli aktivite varsa hemen değiştirin**

## 🛡️ **GitHub Actions Güvenliği**

### **1. Workflow Güvenliği:**
```yaml
# .github/workflows/daily-scraper.yml
env:
  SMTP_SERVER: ${{ secrets.SMTP_SERVER }}
  SMTP_PORT: ${{ secrets.SMTP_PORT }}
  SENDER_EMAIL: ${{ secrets.SENDER_EMAIL }}
  SENDER_PASSWORD: ${{ secrets.SENDER_PASSWORD }}
  RECIPIENTS: ${{ secrets.RECIPIENTS }}
```

### **2. Secrets Yönetimi:**
- **Repository sahibi** sadece secrets'ları görebilir
- **Collaborator'lar** secrets'ları göremez
- **Public repository** → secrets gizli kalır

### **3. Access Control:**
- **Settings** → **Actions** → **General**
- **Workflow permissions**: "Read and write permissions"
- **Allow GitHub Actions**: "Create and approve pull requests"

## 📧 **Email Güvenliği**

### **1. SMTP Güvenliği:**
- **Port 587** (STARTTLS) kullanın
- **TLS/SSL** bağlantı zorunlu
- **Authentication** gerekli

### **2. İçerik Güvenliği:**
- **HTML sanitization** yapın
- **Link validation** ekleyin
- **Spam protection** kullanın

### **3. Alıcı Güvenliği:**
- **Sadece güvenilir** email adresleri
- **BCC kullanmayın** (güvenlik riski)
- **Rate limiting** ekleyin

## 🔍 **Güvenlik Kontrol Listesi**

### **1. Kurulum Öncesi:**
- [ ] 2FA aktif mi?
- [ ] App Password oluşturuldu mu?
- [ ] .gitignore güncellendi mi?
- [ ] Template dosyası oluşturuldu mu?

### **2. Kurulum Sonrası:**
- [ ] email_config.json test edildi mi?
- [ ] GitHub Secrets eklendi mi?
- [ ] Workflow çalışıyor mu?
- [ ] Email gönderiliyor mu?

### **3. Düzenli Kontroller:**
- [ ] App Password güncel mi?
- [ ] GitHub Secrets güncel mi?
- [ ] Güvenlik logları kontrol edildi mi?
- [ ] Şüpheli aktivite var mı?

## 🚨 **Acil Durumlar**

### **1. Şifre Sızıntısı:**
```bash
# 1. Hemen App Password'ü değiştirin
# 2. GitHub Secrets'ı güncelleyin
# 3. email_config.json'ı yeniden oluşturun
# 4. Güvenlik loglarını kontrol edin
```

### **2. Unauthorized Access:**
```bash
# 1. Tüm App Password'leri iptal edin
# 2. GitHub hesabını kilitleyin
# 3. Güvenlik ayarlarını kontrol edin
# 4. Yeni App Password oluşturun
```

### **3. Email Spam:**
```bash
# 1. Rate limiting ekleyin
# 2. Alıcı listesini kontrol edin
# 3. SMTP ayarlarını gözden geçirin
# 4. Spam filtreleri ekleyin
```

## 📚 **Ek Kaynaklar**

### **1. Gmail Güvenlik:**
- [Gmail Güvenlik Merkezi](https://myaccount.google.com/security)
- [2 Adımlı Doğrulama](https://support.google.com/accounts/answer/185839)
- [Uygulama Şifreleri](https://support.google.com/accounts/answer/185833)

### **2. GitHub Güvenlik:**
- [GitHub Security](https://github.com/security)
- [Repository Security](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/security-features)
- [Actions Security](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)

### **3. Email Güvenlik:**
- [SMTP Güvenlik](https://en.wikipedia.org/wiki/SMTP_Authentication)
- [TLS/SSL](https://en.wikipedia.org/wiki/Transport_Layer_Security)
- [Email Spam Protection](https://en.wikipedia.org/wiki/Anti-spam_techniques)

---

**⚠️ ÖNEMLİ**: Bu güvenlik rehberini takip etmek, email sisteminizi ve kişisel bilgilerinizi korur. Güvenlik önlemlerini ihmal etmeyin!
