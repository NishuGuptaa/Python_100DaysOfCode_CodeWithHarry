# Write a program to manipulate pdf files using pyPDF. Your programs should be able to merge multiple pdf files into a single pdf. You are welcome to add more functionalities.
# pyPDF is a free and open-source pure-python PDF library capable of splitting, merging, cropping and transforming the pages of PDF files. It can also add custom data, viewing options and passwords to PDF files. pyPDF can retrieve text and metadata from PDFs as well.

from PyPDF2 import PdfWriter
import os
merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]
if not files:
    print("No PDF files found in the current directory.")
else:
    for pdf in files:
        merger.append(pdf)

merger.write("merged.pdf")
merger.close()
print(f"Merged {len(files)} PDFs into 'merged.pdf'.")