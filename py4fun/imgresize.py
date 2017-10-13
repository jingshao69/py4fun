#!/usr/bin/python

from glob import glob
from PIL import Image
import argparse
import os
import sys

def resize_file(img_file, hsize):
  print "Resizing %s..." %(img_file)
  img = Image.open(img_file)
  width, height = img.size
  # print "width %d height %d" %(width, height)
  vsize = height * hsize/width
  resize_img = img.resize((hsize, vsize))

  file_name, file_ext =os.path.splitext(img_file)
  new_file_name = file_name + "_resize"
  new_img_file = new_file_name + file_ext
  resize_img.save(new_img_file)


parser = argparse.ArgumentParser()
parser.add_argument('--width', '-w', type=int, default=1024, help='image width, default to 1024')
parser.add_argument('files', nargs='+')

args = parser.parse_args()

hsize=args.width

#Resize all the files passed in
for imgfile in args.files:
  file_list = glob(imgfile)
  for file in file_list:
    resize_file(file, hsize)


  

