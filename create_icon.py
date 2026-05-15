# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

def create_icon():
    SIZE = 256

    # ── Arka plan: koyu lacivert → canlı mor ─────────────────────
    base = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    for y in range(SIZE):
        t = y / SIZE
        r = int(20  + (80  - 20)  * t)
        g = int(20  + (20  - 20)  * t)
        b = int(100 + (160 - 100) * t)
        ImageDraw.Draw(base).line([(0, y), (SIZE, y)], fill=(r, g, b, 255))

    # Yuvarlak köşe maskesi
    mask = Image.new("L", (SIZE, SIZE), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, SIZE, SIZE], radius=58, fill=255)
    base.putalpha(mask)

    draw = ImageDraw.Draw(base)

    # ── Merkezdeki parlak daire (arka ışık efekti) ────────────────
    cx, cy = SIZE // 2, SIZE // 2 - 8
    for r in range(90, 0, -1):
        alpha = int(35 * (1 - r / 90))
        draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(160, 120, 255, alpha))

    # ── İnce beyaz çerçeve ────────────────────────────────────────
    draw.rounded_rectangle([3, 3, SIZE-3, SIZE-3],
                           radius=56, outline=(255, 255, 255, 45), width=2)

    # ── Yazı ─────────────────────────────────────────────────────
    font_path = None
    for p in [
        "C:/Windows/Fonts/segoeuib.ttf",
        "C:/Windows/Fonts/calibrib.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
    ]:
        if os.path.exists(p):
            font_path = p
            break

    font = ImageFont.truetype(font_path, 120) if font_path else ImageFont.load_default()
    text = "EH"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    tx = (SIZE - tw) // 2 - bbox[0]
    ty = (SIZE - th) // 2 - bbox[1] - 10

    # Yumuşak gölge
    sh = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    ImageDraw.Draw(sh).text((tx + 4, ty + 6), text, font=font, fill=(0, 0, 60, 120))
    base = Image.alpha_composite(base, sh.filter(ImageFilter.GaussianBlur(5)))

    # Beyaz yazı
    ImageDraw.Draw(base).text((tx, ty), text, font=font, fill=(255, 255, 255, 255))

    # ── Altın aksent çubuğu ───────────────────────────────────────
    draw2 = ImageDraw.Draw(base)
    draw2.rounded_rectangle(
        [SIZE//2 - 40, SIZE - 44, SIZE//2 + 40, SIZE - 36],
        radius=5, fill=(255, 200, 60, 220)
    )

    # ── .ico kaydet ───────────────────────────────────────────────
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.ico")
    base.save(out, format="ICO",
              sizes=[(256,256),(128,128),(64,64),(48,48),(32,32),(16,16)])
    print(f"İkon oluşturuldu: {out}")

if __name__ == "__main__":
    create_icon()
