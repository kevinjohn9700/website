"""
generate_polaroids.py

Creates placeholder "photo" tiles for the polaroid wall -- each one is just
a soft blush background with the SAME flower photo centered on it (no
hearts, no other artwork). Swap the files in /photos/ for real couple
photos later; keep the same filenames or update the list in reveal.html.

Run:
    python3 generate_polaroids.py
Produces:
    photos/photo01.jpg ... photo16.jpg
"""

import os
from PIL import Image

OUT_DIR = "photos"
os.makedirs(OUT_DIR, exist_ok=True)

W, H = 700, 860
BG = (251, 241, 238)
FLOWER_PATH = "assets/flower.png"
COUNT = 16


def main():
    flower = Image.open(FLOWER_PATH).convert("RGBA")
    flower_w = int(W * 0.62)
    flower_h = int(flower_w * flower.height / flower.width)
    flower_resized = flower.resize((flower_w, flower_h), Image.LANCZOS)

    for i in range(COUNT):
        img = Image.new("RGB", (W, H), BG)
        px = (W - flower_w) // 2
        py = (H - flower_h) // 2
        img.paste(flower_resized, (px, py), flower_resized)
        img.save(os.path.join(OUT_DIR, f"photo{i+1:02d}.jpg"), quality=88)

    print(f"Saved {COUNT} placeholder photos to ./{OUT_DIR}/")


if __name__ == "__main__":
    main()
