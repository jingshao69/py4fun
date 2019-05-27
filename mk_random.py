#!/usr/bin/python

import os
import binascii
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('nbytes')

parser.add_argument('-d', '--delimiter', default=':')
args = parser.parse_args()

size=int(args.nbytes)

hex_array=[]
rnd=os.urandom(size)
for i in range(0, len(rnd)):
  hex_code = binascii.b2a_hex(rnd[i])
  hex_array.append(hex_code)

print args.delimiter.join(hex_array)


