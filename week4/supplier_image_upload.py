#!/usr/bin/env python3

import requests
import glob

folder = "supplier-data/images/"
ext = ".jpeg"
url = "http://localhost/upload/"

for file in glob.glob(folder+"/*"+ext):
    with open(file, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
