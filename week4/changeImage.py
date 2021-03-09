#!/usr/bin/python3

from PIL import Image
import glob

folder_in = "supplier-data/images/"
folder_out = "supplier-data/images/"
ext_in = ".tiff"
ext_out = ".jpeg"
image_resolution = (600,400)

for image in glob.glob(folder_in+"/*"+ext_in):
    name = image[len(folder_in):-len(ext_in)]
    im = Image.open(image)
    im.resize(image_resolution).convert('RGB').save(folder_out+name+ext_out)
