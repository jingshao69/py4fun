#!/usr/bin/env python3

from glob import glob
import PyPDF2, os
import argparse
import sys

def add_file(pdf_file):
  print("Adding %s..." %(pdf_file))
  pdfFileObj = open(pdf_file, 'rb')
  pdfReader = PyPDF2.PdfReader(pdfFileObj)
  for pageNum in range(0, len(pdfReader.pages)):
    pageObj = pdfReader.pages[pageNum]
    pdfWriter.add_page(pageObj)

#Create the PdfFileWriter object
pdfWriter = PyPDF2.PdfWriter()

parser = argparse.ArgumentParser()
parser.add_argument('outfile')
parser.add_argument('inFile', nargs='+')

args = parser.parse_args()

for pdfFile in args.inFile:
  if  pdfFile.endswith('.pdf'):
    file_list=glob(pdfFile)
    for file in file_list:
      add_file(file)

print("Writing output to %s..." %(args.outfile))
pdfOutput = open(args.outfile, 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()




  
