#!/usr/bin/env python3
 
import os
from PIL import Image
 
path = '/home/erick/images/'
 
for image in os.listdir(path):
	if '.png' in image and '.' not in image[0]:
		img = Image.open(path + image)
		img.resize((600, 400)).convert("RGB").save(path + image.split('.')[0] + '.jpeg' , 'jpeg')
		img.close()
