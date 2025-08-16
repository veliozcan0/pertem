# 🚨 GitHub Actions Permission Hatası - Hızlı Çözüm

## ❌ **Hata:**
```
Permission to veliozcan0/pertem.git denied to github-actions[bot]
```

## ✅ **Hızlı Çözüm (5 Dakika)**

### **1. GitHub Repository Ayarları (2 dk)**

1. **GitHub'da repository'nize gidin**
2. **Settings** sekmesine tıklayın
3. Sol menüde **Actions** → **General** seçin
4. **Workflow permissions** bölümünde:
   - ✅ **"Read and write permissions"** seçin
   - ✅ **"Allow GitHub Actions to create and approve pull requests"** seçin
5. **Save** butonuna tıklayın

### **2. Güncellenmiş Workflow'u Push Edin (2 dk)**

```bash
# Mevcut değişiklikleri commit edin
git add .
git commit -m "Fix GitHub Actions permissions"
git push origin main
```

### **3. Test Edin (1 dk)**

1. **Actions** sekmesine gidin
2. **"MSB Günlük Veri Çekme"** workflow'unu seçin
3. **"Run workflow"** butonuna tıklayın

## 🔧 **Manuel Tetikleme Seçenekleri**

### **Web Arayüzü:**
- GitHub → Actions → Run workflow

### **CLI (GitHub CLI kurulu ise):**
```bash
gh workflow run "MSB Günlük Veri Çekme"
```

### **Windows Script'leri:**
- `run_scraper.bat` - Çift tıklayın
- `run_scraper.ps1` - PowerShell'de çalıştırın

## 📋 **Kontrol Listesi**

- [ ] Repository Settings → Actions → General → Workflow permissions
- [ ] "Read and write permissions" seçili
- [ ] "Allow GitHub Actions to create and approve pull requests" seçili
- [ ] Save butonuna tıklandı
- [ ] Güncellenmiş workflow push edildi
- [ ] Manuel test yapıldı

## 🚀 **Sonraki Adımlar**

1. **Otomatik çalışma**: Her gün saat 09:00 UTC
2. **Manuel tetikleme**: İstediğiniz zaman
3. **Monitoring**: Actions sekmesinden takip

---

**Not**: Permission hatası çözüldükten sonra workflow otomatik olarak çalışacak ve verileri güncelleyecektir.
