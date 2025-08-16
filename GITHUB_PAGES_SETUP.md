# 🌐 GitHub Pages Kurulum Rehberi

MSB Scraper web arayüzünü herkesin kullanabileceği şekilde yayınlamak için GitHub Pages kullanacağız.

## 🚀 **Kurulum Adımları**

### **1. Repository'yi GitHub'a Yükleyin**

```bash
git add .
git commit -m "Add GitHub Pages web interface"
git push origin main
```

### **2. GitHub Pages'ı Etkinleştirin**

1. **GitHub repository'nizde** **Settings** sekmesine gidin
2. Sol menüde **Pages** seçin
3. **Source** bölümünde:
   - **Deploy from a branch** seçin
   - **Branch**: `main` seçin
   - **Folder**: `/docs` seçin
4. **Save** butonuna tıklayın

### **3. Yayınlanmayı Bekleyin**

- GitHub Pages otomatik olarak yayınlanacak
- Yayınlanma süresi: 2-5 dakika
- URL: `https://veliozcan0.github.io/pertem/`

## 🌍 **Kullanım Linkleri**

### **Ana Linkler:**
- **Web Arayüzü**: https://veliozcan0.github.io/pertem/
- **Doğrudan Tetikleme**: https://veliozcan0.github.io/pertem/?action=trigger

### **GitHub Actions Linkleri:**
- **Actions Ana Sayfa**: https://github.com/veliozcan0/pertem/actions
- **Workflow**: https://github.com/veliozcan0/pertem/actions/workflows/daily-scraper.yml

## 📱 **Paylaşım Örnekleri**

### **1. Sosyal Medya:**
```
🚀 MSB Personel Temin Veri Çekme Aracı
Link üzerinden manuel tetikleme: https://veliozcan0.github.io/pertem/
GitHub: https://github.com/veliozcan0/pertem
```

### **2. Email:**
```
Merhaba,

MSB Personel Temin sitesinden veri çekmek için aşağıdaki linki kullanabilirsiniz:

🌐 Web Arayüzü: https://veliozcan0.github.io/pertem/
🔗 Doğrudan Tetikleme: https://veliozcan0.github.io/pertem/?action=trigger

Bu link herkese açıktır ve herhangi bir kurulum gerektirmez.

İyi çalışmalar!
```

### **3. WhatsApp/Telegram:**
```
🚀 MSB Scraper - Herkes Kullanabilir!

Web Arayüzü: https://veliozcan0.github.io/pertem/
Doğrudan Tetikleme: https://veliozcan0.github.io/pertem/?action=trigger

📱 Mobil uyumlu
🌍 Herkese açık
⚡ Tek tıkla kullanım
```

## 🔧 **Özellikler**

### **1. Otomatik Yönlendirme**
- `?action=trigger` parametresi ile otomatik GitHub Actions'a yönlendirme
- 2 saniye sonra yeni sekmede açılır

### **2. Canlı Durum Takibi**
- GitHub API ile workflow durumu
- Gerçek zamanlı güncellemeler
- Otomatik veri sayısı kontrolü

### **3. Mobil Uyumlu**
- Responsive tasarım
- Tüm cihazlardan erişim
- Touch-friendly butonlar

## 📊 **İstatistikler**

### **Kullanım Metrikleri:**
- GitHub Pages görüntüleme sayısı
- Workflow tetikleme sayısı
- Farklı cihazlardan erişim

### **Takip:**
- Google Analytics eklenebilir
- GitHub Insights
- Repository trafiği

## 🚨 **Güvenlik**

### **1. Public Repository**
- Kod herkese açık
- Güvenlik açığı yok
- Sadece okuma erişimi

### **2. GitHub Actions**
- Sadece repository sahibi tetikleyebilir
- Workflow çalıştırma yetkisi kısıtlı
- Güvenli token kullanımı

## 🔄 **Güncelleme**

### **1. Web Arayüzü Güncelleme:**
```bash
# docs/index.html dosyasını düzenleyin
git add docs/
git commit -m "Update web interface"
git push origin main
```

### **2. Otomatik Yayınlama:**
- GitHub Pages otomatik olarak güncellenir
- Yayınlanma süresi: 1-2 dakika
- Cache temizleme gerekebilir

## 📞 **Destek**

### **1. Yaygın Sorunlar:**
- **404 Hatası**: `/docs` klasörünün doğru olduğundan emin olun
- **Yayınlanmıyor**: GitHub Pages ayarlarını kontrol edin
- **Cache Sorunu**: Tarayıcı cache'ini temizleyin

### **2. İletişim:**
- GitHub Issues: Repository'de issue açın
- GitHub Discussions: Topluluk desteği
- Email: Repository sahibi ile iletişim

---

**Not**: GitHub Pages kurulumu tamamlandıktan sonra web arayüzü herkese açık olacak ve link üzerinden paylaşılabilir.
