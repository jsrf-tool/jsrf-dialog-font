#!/usr/bin/python3

#montage *.png -tile 17x10 -geometry +0+0 poke.png

from PIL import Image
from os import mkdir
import shutil, tempfile, os, pathlib

sprite_sheet_path = "jsrf-alphanumeric.png"

output_ext = 'bmp'
output_dir = pathlib.Path(f'./{output_ext}').resolve()


output_dir.mkdir(exist_ok=True)
for f in output_dir.iterdir():
  f.unlink()

sheet = Image.open(sprite_sheet_path)
count = 0
threshold = 100

x_margin = (0, 0)
y_margin = (0, 0)

x, y = 0, y_margin[0]
w, h = 21, 34

x_max = sheet.width  - x_margin[1]
y_max = sheet.height - y_margin[1]

chars = """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz"""
char_iter = iter(chars)


with tempfile.TemporaryDirectory(dir=os.getcwd()) as directory:
  image_dir = pathlib.Path(directory)

  while y < y_max:
    yh = y + h
    x=x_margin[0]
    while x < x_max:
      xw = x + w
      sprite = sheet.crop((x, y, xw, yh))
      # sprite = sprite.point(lambda p: p*2 if p < threshold else 255)  # binary threshold
      # sprite = sprite.resize(map(lambda x: x*2, sprite.size), resample=Image.NEAREST) #enlarge
      sprite = sprite.resize(map(lambda x: x*2, sprite.size), resample=Image.BILINEAR) #enlarge
      sprite = sprite.resize(map(lambda x: x*2, sprite.size), resample=Image.ANTIALIAS) #enlarge

      try:
        char_name = next(char_iter)
      except StopIteration:
        char_name = ' '
      char_ord = f'{ord(char_name):04d}'

      sprite_path = image_dir / f"{char_ord}.{output_ext}"
      sprite.save(sprite_path)

      print(f"{char_name} -> {sprite_path}")

      count += 1
      x = xw
    y = yh

  for f in image_dir.iterdir():
    shutil.move(f, output_dir)

