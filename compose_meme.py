#!/usr/bin/env python3
"""Compose the gta6-meme-x-01 meme (run in-session by the agent).

Base scene: AI-generated original Vice City-style illustration
(entry/assets/media-generation-gta6-meme-base-0-*.webp).
Ghost: official make.fun press-kit mark (entry/assets/makefun-ghost.png),
pasted into the convertible's back seat so it rides along in the scene.
Captions: DejaVu Sans Bold, white with black stroke (classic meme style).
Output: entry/meme.png (1080x1080) + entry/meme-480.png (judge-size preview).
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE = "entry/assets/media-generation-gta6-meme-base-0-bf625651-5232-401c-8a62-a98b0f64132f.webp"
GHOST = "entry/assets/makefun-ghost.png"
OUT = "entry/meme.png"
OUT480 = "entry/meme-480.png"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

W = 1080
img = Image.open(BASE).convert("RGB").resize((W, W), Image.LANCZOS)

# --- ghost into the back seat (teal rear bench, right of the couple) ---
ghost = Image.open(GHOST).convert("RGBA")
g = 200  # ghost size
ghost = ghost.resize((g, g), Image.LANCZOS)
# soft drop shadow: black silhouette, blurred, offset down-right
shadow = Image.new("RGBA", (g + 24, g + 24), (0, 0, 0, 0))
sil = Image.new("RGBA", (g, g), (0, 0, 0, 0))
alpha = ghost.split()[3].point(lambda a: int(a * 0.55))
sil.putalpha(alpha)
shadow.paste(sil, (12, 14), sil)
shadow = shadow.filter(ImageFilter.GaussianBlur(6))
gx, gy = 700, 470  # top-left of ghost; sits on the rear bench
img.paste(shadow, (gx - 12, gy - 14), shadow)
img.paste(ghost, (gx, gy), ghost)

# --- captions ---
draw = ImageDraw.Draw(img)


def fit_font(text, max_w, start):
    size = start
    while size > 20:
        f = ImageFont.truetype(FONT, size)
        if draw.textlength(text, font=f) <= max_w:
            return f
        size -= 2
    return ImageFont.truetype(FONT, 20)


def draw_line(text, y, size, fill="white", stroke=8):
    f = fit_font(text, W - 80, size)
    draw.text((W // 2, y), text, font=f, fill=fill, anchor="ma",
              stroke_width=stroke, stroke_fill="black")


# top: the hook (sky area)
draw_line("WAITED 13 YEARS", 55, 84)
draw_line("FOR GTA 6", 150, 84)
# bottom: the punchline + make.fun pitch (road area)
draw_line("MY AI AGENT MADE MONEY", 845, 72)
draw_line("ON MAKE.FUN", 930, 72)

img.save(OUT, "PNG")
img.resize((480, 480), Image.LANCZOS).save(OUT480, "PNG")
print("saved", OUT, img.size, "| preview", OUT480)
