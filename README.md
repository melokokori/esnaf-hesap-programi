# Esnaf Hesap Programı

Küçük esnaf ve işletmeler için geliştirilmiş masaüstü hesap takip uygulaması.  
Python + CustomTkinter ile yazılmıştır, kurulum gerektirmeden `.exe` olarak dağıtılabilir.

## Özellikler

- **Müşteri Hesapları** — alışveriş ve borç ödeme takibi, bakiye görüntüleme
- **Günlük Satışlar** — marka / ürün türü bazlı satış kaydı, filtreli raporlama
- **Toplu Giriş** — tek müşteriye sepet mantığıyla çoklu ürün girişi
- **Arama & Filtre** — isim/telefon arama, borçlular / tümü / arşiv filtresi
- **Arşivleme** — sıfır bakiyeli müşterileri arşive taşı
- **İşletme Adı** — ayarlar ekranından özelleştirilebilir (ilk çalıştırmada sorulur)

## Kurulum (Geliştirici)

```bash
pip install -r requirements.txt
python app.py
```

## Dağıtım (.exe)

```bash
pip install pyinstaller
pyinstaller --noconfirm --onedir --windowed --icon=icon.ico --name "HesapProgrami" --distpath dist app.py
```

Oluşan `dist/HesapProgrami/` klasörünü olduğu gibi kopyalayın.  
`HesapProgrami.exe`'ye çift tıklamak yeterlidir — Python kurulumu gerekmez.

## Veritabanı

Veriler `hesap.db` (SQLite) dosyasında saklanır.  
Yedek almak için bu dosyayı kopyalamak yeterlidir.

## Ekran Görüntüsü

> *(eklenecek)*

## Lisans

MIT
