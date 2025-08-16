# GitHub Actions ile Otomatik MSB Veri Çekme

Bu proje, GitHub Actions kullanarak MSB Personel Temin sitesinden günlük otomatik veri çekme işlemini gerçekleştirir.

## 🚀 Özellikler

- **Günlük Otomatik Çalışma**: Her gün saat 09:00 UTC'de otomatik çalışır
- **Manuel Tetikleme**: İstediğiniz zaman manuel olarak çalıştırabilirsiniz
- **Otomatik Commit**: Çekilen veriler otomatik olarak commit edilir
- **Yedekleme**: Her çalıştırmada tarihli yedek dosyalar oluşturulur
- **Hata Yönetimi**: Başarısız çalışmalar için detaylı loglar

## 📋 Kurulum Adımları

### 1. Repository'yi GitHub'a Yükleyin

```bash
git init
git add .
git commit -m "Initial commit: MSB Scraper with GitHub Actions"
git branch -M main
git remote add origin https://github.com/KULLANICI_ADINIZ/REPO_ADINIZ.git
git push -u origin main
```

### 2. GitHub Actions'ı Etkinleştirin

1. GitHub repository'nizde **Actions** sekmesine gidin
2. **Configure** butonuna tıklayın
3. **Workflows** bölümünde "MSB Günlük Veri Çekme" workflow'unu göreceksiniz

### 3. Workflow'u İlk Kez Çalıştırın

1. **Actions** sekmesinde "MSB Günlük Veri Çekme" workflow'unu seçin
2. **Run workflow** butonuna tıklayın
3. **Run workflow** butonuna tekrar tıklayın

## ⏰ Zamanlama

Workflow şu zamanlarda çalışır:

- **Otomatik**: Her gün saat 09:00 UTC (Türkiye saati ile 12:00)
- **Manuel**: İstediğiniz zaman Actions sekmesinden tetikleyebilirsiniz

### Zamanlama Değiştirme

`.github/workflows/daily-scraper.yml` dosyasındaki cron ifadesini değiştirerek zamanlamayı ayarlayabilirsiniz:

```yaml
schedule:
  # Her gün saat 09:00 UTC
  - cron: '0 9 * * *'
  
  # Her gün saat 06:00 UTC (Türkiye saati ile 09:00)
  - cron: '0 6 * * *'
  
  # Her 6 saatte bir
  - cron: '0 */6 * * *'
```

## 📁 Dosya Yapısı

```
.github/
└── workflows/
    └── daily-scraper.yml      # GitHub Actions workflow
scraper.py                     # Ana scraper (yerel kullanım)
scraper-actions.py             # GitHub Actions için optimize edilmiş scraper
requirements.txt                # Yerel geliştirme için
requirements-actions.txt        # GitHub Actions için
data/                          # Çekilen veriler (otomatik oluşur)
```

## 🔧 Manuel Çalıştırma

### GitHub Actions Sekmesinden

1. Repository'nizde **Actions** sekmesine gidin
2. **MSB Günlük Veri Çekme** workflow'unu seçin
3. **Run workflow** butonuna tıklayın
4. **Run workflow** butonuna tekrar tıklayın

### GitHub CLI ile

```bash
gh workflow run "MSB Günlük Veri Çekme"
```

## 📊 Çalışma Durumu Takibi

### Başarılı Çalışmalar

- ✅ Yeşil tik işareti
- Veriler `data/` klasörüne kaydedildi
- Otomatik commit oluşturuldu

### Başarısız Çalışmalar

- ❌ Kırmızı X işareti
- Detaylı hata logları mevcut
- **Actions** sekmesinden logları inceleyebilirsiniz

## 🐛 Hata Giderme

### Yaygın Hatalar

1. **Permission Hatası**
   ```
   Error: fatal: could not read Username for 'https://github.com'
   ```
   **Çözüm**: Repository'de **Settings > Actions > General > Workflow permissions** bölümünde "Read and write permissions" seçin.

2. **Dependency Hatası**
   ```
   ModuleNotFoundError: No module named 'requests'
   ```
   **Çözüm**: `requirements-actions.txt` dosyasının doğru olduğundan emin olun.

3. **Git Hatası**
   ```
   Error: fatal: not a git repository
   ```
   **Çözüm**: Workflow'da `actions/checkout@v4` action'ının doğru çalıştığından emin olun.

### Log İnceleme

1. **Actions** sekmesine gidin
2. Başarısız workflow'u seçin
3. **Build** adımına tıklayın
4. Detaylı logları inceleyin

## 🔒 Güvenlik

### Repository Ayarları

1. **Settings > Actions > General**
   - "Allow all actions and reusable workflows" seçin
   - "Allow GitHub Actions to create and approve pull requests" seçin

2. **Settings > Actions > General > Workflow permissions**
   - "Read and write permissions" seçin
   - "Allow GitHub Actions to create and approve pull requests" seçin

### Secrets ve Environment Variables

Bu proje için ek secrets gerekmez, `GITHUB_TOKEN` otomatik olarak sağlanır.

## 📈 Monitoring ve Bildirimler

### Email Bildirimleri

GitHub'da **Settings > Notifications** bölümünden email bildirimlerini ayarlayabilirsiniz.

### Slack/Discord Entegrasyonu

İleride Slack veya Discord webhook'ları ekleyerek bildirim gönderebiliriz.

## 🚀 Gelişmiş Özellikler

### Çoklu Zamanlama

```yaml
schedule:
  # Sabah 09:00
  - cron: '0 9 * * *'
  # Akşam 18:00
  - cron: '0 18 * * *'
```

### Koşullu Çalıştırma

```yaml
jobs:
  scrape-msb-data:
    runs-on: ubuntu-latest
    if: github.repository == 'KULLANICI_ADINIZ/REPO_ADINIZ'
```

### Environment Variables

```yaml
env:
  PYTHON_VERSION: '3.11'
  TIMEOUT: 30
```

## 📞 Destek

Sorun yaşarsanız:

1. **Issues** sekmesinden yeni issue açın
2. **Actions** sekmesinden logları inceleyin
3. GitHub Community'den yardım alın

## 🔄 Güncelleme

Workflow'u güncellemek için:

1. `.github/workflows/daily-scraper.yml` dosyasını düzenleyin
2. Commit ve push yapın
3. GitHub Actions otomatik olarak yeni versiyonu kullanacak

---

**Not**: Bu workflow her çalıştığında `data/` klasöründeki verileri günceller ve otomatik olarak commit eder. Veri geçmişini korumak için her çalıştırmada yedek dosyalar oluşturulur.
