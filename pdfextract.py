#!/usr/bin/python

import PyPDF2, os
import argparse
import sys

def check_range(page):
  for i in range(0, len(page_ranges)):
    if (page_ranges[i].find('-') == -1):
      int_page = int(page_ranges[i])
      if ( int_page == page):
        return 1
    else:
      range2 = page_ranges[i].split('-')
      int_min = int(range2[0])
      int_max = int(range2[1])
      if ((page >=int_min) and (page <= int_max)):
        return 1

  return 0



#Create the PdfFileWriter object
pdfWriter = PyPDF2.PdfFileWriter()

parser = argparse.ArgumentParser()
parser.add_argument('outFile')
parser.add_argument('inFile')
parser.add_argument('range')

args = parser.parse_args()

page_ranges =args.range.split(',')

if  args.inFile.endswith('.pdf'):
  pdfFileObj = open(args.inFile, 'rb')
  pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
  for pageNum in range(0, pdfReader.numPages):
    if check_range(pageNum+1):
      pageObj = pdfReader.getPage(pageNum)
      pdfWriter.addPage(pageObj)

print "Writing output to %s..." %(args.outFile)
pdfOutput = open(args.outFile, 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()




  
