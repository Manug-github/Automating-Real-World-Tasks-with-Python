#! /usr/bin/env python3

import glob
import os
import requests

external_IP = "104.198.129.151"
folder = "supplier-data/descriptions/"
ext = ".txt"

address = "http://{}/fruits".format(external_IP)
data_json = []

for file in glob.glob(folder+"/*"+ext):
    
    d = {}
    with open file as f:
        lines = [line.strip() for line in f.readlines()]
        d["name"]=lines[0]
        d["weight"]=int(lines[1].split()[0])
        d["description"]=lines[2]
        name_image = file.split("/")[-1].replace(".txt",".jpeg")
        d["image_name"]=name_image

    response = requests.post(address, json=data_json)
    response.raise_for_status()