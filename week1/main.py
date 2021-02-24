#!/usr/bin/python3

from PIL import Image
import glob

folder_in = "images/"
folder_out = "/opt/icons/"

ext_out = "JPEG"

images = glob.glob(folder_in+"*")
for image in images:
    name = image[len(folder_in)+1:]

    im = Image.open(image)
    im.rotate(90).resize((128,128)).convert('RGB').save(folder_out + "/" + name, ext_out)

