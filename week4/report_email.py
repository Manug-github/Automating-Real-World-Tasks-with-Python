#!/usr/bin/env python3

import reports
import datetime
import glob
import emails
import os

def extract_data(folder,ext):
    data = []
    for file in glob.glob(folder+"/*"+ext):
        data.append("")
        with open(file) as f:
            lines = [line.strip() for line in f.readlines()]
            data.append("name: "+lines[0])
            data.append("weight: "+lines[1])
    return data

def main():
    folder = "supplier-data/descriptions/"
    ext = ".txt"
    attachment = "/tmp/processed.pdf"
    mydate = datetime.datetime.now()
    title = "Processed Update on {} {}, {}".format(mydate.strftime("%B"),mydate.day,mydate.year)
    paragraph = extract_data(folder,ext)
    reports.generate_report(attachment, title, paragraph)

    # TODO: send the PDF report as an email attachment
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body =  "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate(sender, receiver, subject, body, attachment)
    emails.send(message)


if __name__ == "__main__":
    main()