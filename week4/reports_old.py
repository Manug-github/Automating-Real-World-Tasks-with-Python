#! /usr/bin/env python3

import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


def generate_report(folder, title, lines):
    c = canvas.Canvas("test.pdf")
    c.setFont('Helvetica-Bold', 14)
    c.drawString(100, 750, title)
    c.setFont('Helvetica', 10)
    textobject = c.beginText(100, 700)
    for line in lines:
        textobject.textLine(line.strip())
    c.drawText(textobject)
    c.save()


"""folder = "test.pdf"
title = "casa"
summary = ["perro","","gato"]
generate_pdf(folder, title, summary)"""