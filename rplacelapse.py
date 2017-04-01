#!/usr/bin/env python3

from PIL import Image
import os

colors = [
    (255, 255, 255),
    (228, 228, 228),
    (136, 136, 136),
    (34, 34, 34),
    (255, 167, 209),
    (229, 0, 0),
    (229, 149, 0),
    (160, 106, 66),
    (229, 217, 0),
    (148, 224, 68),
    (2, 190, 1),
    (0, 211, 221),
    (0, 131, 199),
    (0, 0, 234),
    (207, 110, 228),
    (130, 0, 128)
]

frame = 1
while True:
    filename = "board-bitmap.{}".format(frame)
    if not os.path.isfile(filename):
        break
    print("frame: {}".format(frame))
    img = Image.new('P', (1000, 1000))
    # Set image color palette. PIL palettes have all colors
    # concatenated into one list: (255,255,255,228,228,228,...)
    img.putpalette(sum(colors, ()))
    pixels = img.load()
    with open(filename, "rb") as f:
        for y in range(1000):
            for x in range(500):
                datum = ord(f.read(1))
                color1 = datum >> 4
                color2 = datum - (color1 << 4)
                pixels[x*2,     y] = color1
                pixels[x*2 + 1, y] = color2
    img.save(filename + ".png")
    frame += 1
