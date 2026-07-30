"""
generate_pattern.py

Builds the two curtain panels (left.png / right.png) by tiling the SAME
flower photo (assets/flower.png) at random size/rotation/position until
the canvas is fully covered -- no other flower art, no other shapes.

Run:
    python3 generate_pattern.py
Produces:
    left.png, right.png
"""

import math
import random
from PIL import Image

random.seed(11)

PANEL_W, PANEL_H = 1000, 1200
CANVAS_W, CANVAS_H = PANEL_W * 2, PANEL_H

FLOWER_PATH = "assets/flower.png"
BG_COLOR = (251, 241, 238, 255)  # soft blush, matches the rest of the site


def build_scene():
    flower = Image.open(FLOWER_PATH).convert("RGBA")
    canvas = Image.new("RGBA", (CANVAS_W, CANVAS_H), BG_COLOR)

    spacing = 150  # smaller than flower size -> dense overlap, no gaps
    flowers = []
    y = -spacing
    row = 0
    while y < CANVAS_H + spacing:
        x_off = (spacing / 2) if row % 2 else 0
        x = -spacing + x_off
        while x < CANVAS_W + spacing:
            jitter_x = random.uniform(-0.4, 0.4) * spacing
            jitter_y = random.uniform(-0.4, 0.4) * spacing
            size = random.uniform(1.3, 1.9) * spacing
            rot = random.uniform(0, 360)
            flowers.append((x + jitter_x, y + jitter_y, size, rot))
            x += spacing
        y += spacing * 0.82
        row += 1

    # bigger flowers first (further back), smaller/newer ones layer on top
    flowers.sort(key=lambda f: -f[2])

    for (fx, fy, size, rot) in flowers:
        f = flower.resize((int(size), int(size)), Image.LANCZOS)
        f = f.rotate(rot, expand=True, resample=Image.BICUBIC)
        canvas.alpha_composite(f, (int(fx - f.width / 2), int(fy - f.height / 2)))

    return canvas.convert("RGB")


def main():
    scene = build_scene()
    left = scene.crop((0, 0, PANEL_W, PANEL_H))
    right = scene.crop((PANEL_W, 0, CANVAS_W, PANEL_H))
    print("Saved left.png and right.png", left.size, right.size)


if __name__ == "__main__":
    main()
