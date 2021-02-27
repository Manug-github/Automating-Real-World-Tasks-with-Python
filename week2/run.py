#! /usr/bin/env python3

import os
import requests
import json

folder = "/data/feedback"
IP_address = "XXXX"
ext = ".txt"
address = "http://{}/feedback".format(IP_address)


def read_file_to_dict(file):
    """Extract information from file, and convert to dictionary"""
    d = {}
    keys = ['title', 'name', 'date', "feedback"]
    with open(file, "r") as f:
        lines = f.readlines()
        if len(lines)!=len(keys):
            raise Exception('The number of lines in file:\n {} is {}, must be {}'.format(file, len(lines),len(keys)))
        for i in range(len(lines)):
            d[keys[i]] = lines[i].strip()    
    return d


def request_files():
    for file in os.listdir(folder):
        if file.endswith(ext):
            d = read_file_to_dict(folder+"/"+file)
            response = requests.post(address, json=d)
            response.raise_for_status()


def main():
    request_files()


if __name__ == "__main__":
    main()
