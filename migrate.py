import sqlite3, os
con = sqlite3.connect(os.path.join(os.path.dirname(__file__), "hesap.db"))
cur = con.cursor()
cols = [r[1] for r in cur.execute("PRAGMA table_info(gunluk_satis)").fetchall()]
if "marka" not in cols:
    cur.execute("ALTER TABLE gunluk_satis ADD COLUMN marka TEXT DEFAULT ''")
if "urun_turu" not in cols:
    cur.execute("ALTER TABLE gunluk_satis ADD COLUMN urun_turu TEXT DEFAULT ''")
cur.executescript("""
    CREATE TABLE IF NOT EXISTS markalar (
        id  INTEGER PRIMARY KEY AUTOINCREMENT,
        adi TEXT NOT NULL UNIQUE
    );
    CREATE TABLE IF NOT EXISTS urun_turleri (
        id  INTEGER PRIMARY KEY AUTOINCREMENT,
        adi TEXT NOT NULL UNIQUE
    );
""")
con.commit()
con.close()
print("Veritabani guncellendi.")
