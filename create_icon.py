# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import os, math

def create_icon():
    SIZE = 256
    MARGIN = 0

    # ── Gradient arka plan ──────────────────────────────────────
    base = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    grad = ImageDraw.Draw(base)

    top    = (15, 82, 186)   # koyu mavi
    bottom = (0, 176, 155)   # teal-yeşil

    for y in range(SIZE):
        t = y / SIZE
        r = int(top[0] + (bottom[0] - top[0]) * t)
        g = int(top[1] + (bottom[1] - top[1]) * t)
        b = int(top[2] + (bottom[2] - top[2]) * t)
        grad.line([(0, y), (SIZE, y)], fill=(r, g, b, 255))

    # ── Yuvarlak köşe maskesi ────────────────────────────────────
    mask = Image.new("L", (SIZE, SIZE), 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        [MARGIN, MARGIN, SIZE - MARGIN, SIZE - MARGIN],
        radius=52, fill=255
    )
    base.putalpha(mask)

    # ── Parlak iç çerçeve (ince beyaz kenar) ────────────────────
    border = ImageDraw.Draw(base)
    border.rounded_rectangle(
        [MARGIN + 4, MARGIN + 4, SIZE - MARGIN - 4, SIZE - MARGIN - 4],
        radius=48, outline=(255, 255, 255, 40), width=3
    )

    # ── Yazı ────────────────────────────────────────────────────
    draw = ImageDraw.Draw(base)

    font_path = None
    for p in [
        "C:/Windows/Fonts/arialbd.ttf",
        "C:/Windows/Fonts/calibrib.ttf",
        "C:/Windows/Fonts/segoeuib.ttf",
        "C:/Windows/Fonts/verdanab.ttf",
    ]:
        if os.path.exists(p):
            font_path = p
            break

    font_size = 118
    if font_path:
        from PIL import ImageFont
        font = ImageFont.truetype(font_path, font_size)
    else:
        font = ImageFont.load_default()

    text = "EH"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = (SIZE - tw) // 2 - bbox[0]
    ty = (SIZE - th) // 2 - bbox[1] - 4

    # Gölge
    draw.text((tx + 4, ty + 5), text, font=font, fill=(0, 0, 0, 70))
    # Yazı
    draw.text((tx, ty), text, font=font, fill=(255, 255, 255, 255))

    # ── Alt ince çizgi aksanı ────────────────────────────────────
    draw.line([(SIZE//2 - 44, SIZE - 52), (SIZE//2 + 44, SIZE - 52)],
              fill=(255, 255, 255, 130), width=3)

    # ── .ico kaydet ─────────────────────────────────────────────
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.ico")
    base.save(out, format="ICO",
              sizes=[(256,256),(128,128),(64,64),(48,48),(32,32),(16,16)])
    print(f"İkon oluşturuldu: {out}")

if __name__ == "__main__":
    create_icon()
