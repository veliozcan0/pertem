# MSB Personel Temin Sitesi Veri Çekme Aracı

Bu Python script'i, Millî Savunma Bakanlığı Personel Temin Sistemi sitesinden "GÜNCEL TEMİNLER" ve "GÜNCEL DUYURULAR" verilerini otomatik olarak çeker.

## Özellikler

- **GÜNCEL TEMİNLER**: Personel temin ilanları ve detayları
- **GÜNCEL DUYURULAR**: Duyuru başlıkları, tarihleri ve linkleri
- **JSON Export**: Çekilen verileri JSON formatında kaydetme
- **Türkçe Karakter Desteği**: UTF-8 encoding ile Türkçe karakterleri düzgün işleme
- **Hata Yönetimi**: Bağlantı ve parse hatalarını yakalama
- **Veri Filtreleme**: Anahtar kelimeye göre veri filtreleme
- **Otomatik Yedekleme**: Tarihli yedek dosyalar oluşturma
- **Veri Analizi**: Temel istatistikler ve analiz

## Kurulum

1. Python 3.7 veya üzeri sürümünü yükleyin
2. Gerekli kütüphaneleri yükleyin:

```bash
pip install -r requirements.txt
```

## Kullanım

### Temel Kullanım

Script'i çalıştırmak için:

```bash
python scraper.py
```

### Gelişmiş Kullanım

Örnek kullanım senaryoları için:

```bash
python example_usage.py
```

### Programatik Kullanım

```python
from scraper import fetch_msb_data, filter_data_by_keyword, save_to_json

# Veri çek
data = fetch_msb_data()

# Filtrele
kara_kuvvetleri = filter_data_by_keyword(data, "KARA KUVVETLERİ")

# Kaydet
save_to_json(kara_kuvvetleri, "kara_kuvvetleri.json")
```

## Çıktı Formatı

### GÜNCEL TEMİNLER
```json
{
  "başlık": "MİLLÎ SAVUNMA BAKANLIĞI SÖZLEŞMELİ BİLİŞİM PERSONELİ TEMİNİ",
  "açıklama": "MİLLÎ SAVUNMA BAKANLIĞI SÖZLEŞMELİ BİLİŞİM PERSONELİ TEMİNİ",
  "tarih": "04.08.2025",
  "link": "/AnaSayfa/DuyuruDetay/?id=cddf9320-b4a7-4d30-ad18-63441edb55eb"
}
```

### GÜNCEL DUYURULAR
```json
{
  "ay": "Ağustos",
  "gün": "14",
  "gün_adı": "Perşembe",
  "başlık": "KARA KUVVETLERİ KOMUTANLIĞI UZMAN ERBAŞ ADAYI KESİN KAYIT/EĞİTİM İLANI",
  "tarih": "14.08.2025",
  "link": "/AnaSayfa/DuyuruDetay/?id=52755e07-1f07-406e-9c48-818359dd08fc"
}
```

## Dosya Yapısı

```
pertem/
├── scraper.py                    # Ana script dosyası
├── example_usage.py             # Örnek kullanım dosyası
├── requirements.txt             # Gerekli Python kütüphaneleri
├── README.md                    # Bu dosya
├── data/                        # Veri klasörü
│   ├── msb_data.json           # Ana veri dosyası
│   ├── msb_data_YYYYMMDD_HHMMSS.json  # Tarihli yedekler
│   ├── kara_kuvvetleri_duyurulari.json  # Filtrelenmiş veriler
│   ├── bilisim_teminleri.json  # Filtrelenmiş veriler
│   └── msu_duyurulari.json     # Filtrelenmiş veriler
└── msb_data.json               # Eski veri dosyası (root'ta)
```

## Özellikler Detayı

### Veri Filtreleme
- Anahtar kelimeye göre temin ve duyuru filtreleme
- Büyük/küçük harf duyarsız arama
- Filtrelenmiş verileri ayrı dosyalara kaydetme

### Otomatik Yedekleme
- Her çalıştırmada tarihli yedek dosya oluşturma
- Veri klasöründe organize edilmiş dosya yapısı
- Veri kaybını önleme

### Hata Yönetimi
- Bağlantı hatalarını yakalama
- Parse hatalarını güvenli şekilde işleme
- Detaylı hata mesajları

## Güvenlik ve Yasal Uyarılar

- Bu script sadece eğitim ve kişisel kullanım amaçlıdır
- Site kullanım şartlarına uygun kullanım yapılmalıdır
- Aşırı istek gönderimi yapılmamalıdır
- Telif haklarına saygı gösterilmelidir

## Hata Giderme

### Yaygın Hatalar:

1. **Bağlantı Hatası**: İnternet bağlantınızı kontrol edin
2. **Parse Hatası**: Site yapısı değişmiş olabilir, script güncellenmelidir
3. **Encoding Hatası**: Türkçe karakterler düzgün görünmüyorsa encoding ayarlarını kontrol edin
4. **Kütüphane Hatası**: `pip install -r requirements.txt` komutunu çalıştırın

### Performans İpuçları:

- Script'i çok sık çalıştırmayın
- Büyük veri setleri için filtreleme kullanın
- Yedek dosyaları düzenli olarak temizleyin

## Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Commit yapın (`git commit -m 'Add some AmazingFeature'`)
4. Push yapın (`git push origin feature/AmazingFeature`)
5. Pull Request oluşturun

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## İletişim

Sorularınız için issue açabilir veya pull request gönderebilirsiniz.

## Güncelleme Geçmişi

- **v1.0**: Temel veri çekme özelliği
- **v1.1**: GÜNCEL DUYURULAR desteği eklendi
- **v1.2**: Veri filtreleme ve yedekleme özellikleri eklendi
- **v1.3**: Örnek kullanım dosyası ve gelişmiş hata yönetimi
