# Esnaf Hesap Programı

Küçük esnaf ve işletmeler için geliştirilmiş masaüstü hesap takip uygulaması.  
Python + CustomTkinter ile yazılmıştır.

---

## İndirme (Hazır Kurulum — Python gerekmez)

**[⬇ EsnafHesapProgrami_v1.0.0.zip — İndir](https://github.com/melokokori/esnaf-hesap-programi/releases/latest)**

1. ZIP'i indirip bir klasöre çıkartın
2. `Kisayol Olustur.bat` → çift tıkla → masaüstünde kısayol hazır
3. Kısayola çift tıkla → program açılır, işletme adınızı girin

> Windows 10 / 11 üzerinde çalışır. Python kurulumu **gerekmez.**

---

## Özellikler

- **Müşteri Hesapları** — alışveriş ve borç ödeme takibi, bakiye görüntüleme
- **Günlük Satışlar** — marka / ürün türü bazlı satış kaydı, filtreli raporlama
- **Toplu Giriş** — tek müşteriye sepet mantığıyla çoklu ürün girişi
- **Excel Raporu** — borçlular, satışlar ve tüm işlemler (3 sayfalı)
- **Yedekleme** — tek tıkla yedek al / geri yükle
- **İşletme Adı** — ilk çalıştırmada sorulur, Ayarlar'dan değiştirilebilir
- **Klavye kısayolları** — Ctrl+S kaydet, Ctrl+R rapor, Ctrl+H hakkında

---

## Geliştirici Kurulumu (Kaynak Koddan Çalıştırma)

```bash
pip install -r requirements.txt
python app.py
```

### Exe Derleme

```bash
pip install pyinstaller
pyinstaller --noconfirm --onedir --windowed --icon=icon.ico --name "EsnafHesapProgrami" --distpath dist app.py
```

---

## Veritabanı

Veriler `hesap.db` (SQLite) dosyasında saklanır. Yedek almak için bu dosyayı kopyalamak yeterlidir.

---

## Lisans & İletişim

© 2025 melokokori — Tüm hakları saklıdır.  
Bu yazılım izinsiz kopyalanamaz ve dağıtılamaz.

**GitHub:** https://github.com/melokokori/esnaf-hesap-programi
