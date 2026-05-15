# Esnaf Hesap Programı — Small Business Account Tracker

> 🇹🇷 Türkçe | 🇬🇧 [English below](#english)

---

## 🇹🇷 Türkçe

Küçük esnaf ve işletmeler için geliştirilmiş masaüstü hesap takip uygulaması.

### İndirme (Python gerekmez)

**[⬇ EsnafHesapProgrami_v1.0.0.zip — İndir](https://github.com/melokokori/esnaf-hesap-programi/releases/latest)**

1. ZIP'i indirip bir klasöre çıkartın
2. `Kisayol Olustur.bat` → çift tıkla → masaüstünde kısayol hazır
3. Kısayola çift tıkla → program açılır, işletme adınızı girin

> Windows 10 / 11 üzerinde çalışır.

### Özellikler

- Müşteri hesabı ve borç takibi
- Günlük satış kaydı (marka / ürün türü)
- Toplu alışveriş girişi
- Excel rapor çıktısı (3 sayfa)
- Yedek al / geri yükle
- İşletme adı özelleştirilebilir
- Klavye kısayolları: Ctrl+S, Ctrl+R, Ctrl+H

### Geliştirici Kurulumu

```bash
pip install -r requirements.txt
python app.py
```

---

## 🇬🇧 English <a name="english"></a>

A lightweight desktop application for small businesses to track customer debts and daily sales.  
Built with Python + CustomTkinter + SQLite.

### Download (No Python required)

**[⬇ Download EsnafHesapProgrami_v1.0.0.zip](https://github.com/melokokori/esnaf-hesap-programi/releases/latest)**

1. Extract the ZIP to any folder
2. Double-click `Kisayol Olustur.bat` → shortcut created on your desktop
3. Double-click the shortcut → app opens, enter your business name

> Works on Windows 10 / 11. No Python installation needed.

### Features

- Customer account & debt tracking
- Daily sales log (brand / product type)
- Bulk entry with shopping cart
- Excel report export (3 sheets: debtors, sales, transactions)
- One-click backup & restore
- Customizable business name (set on first launch, editable in Settings)
- Keyboard shortcuts: Ctrl+S save, Ctrl+R report, Ctrl+H about

### Developer Setup

```bash
pip install -r requirements.txt
python app.py
```

### Build Executable

```bash
pip install pyinstaller
pyinstaller --noconfirm --onedir --windowed --icon=icon.ico --name "EsnafHesapProgrami" --distpath dist app.py
```

### Tech Stack

| Component | Library |
|-----------|---------|
| UI | CustomTkinter |
| Database | SQLite3 |
| Reports | openpyxl |
| Packaging | PyInstaller |

---

## License

© 2025 melokokori — All rights reserved.  
This software may not be copied or distributed without permission.
