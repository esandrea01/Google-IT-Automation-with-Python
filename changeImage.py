#!/usr/bin/env python3
from PIL import Image
import os

arr = os.listdir()
for file in arr:
 if file.endswith('tiff'):
  im = Image.open(file)
  new_im = im.resize((600,400))
  new_im.convert('RGB').save('/supplier-data/images'+ file +'.jpeg')
