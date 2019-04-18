#!/usr/bin/python

import os
import binascii
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('nbytes')

args = parser.parse_args()

size=int(args.nbytes)

rnd=os.urandom(size)
rnd_hex= binascii.b2a_hex(rnd)

for i in range(0, size):
  print "0x%s," %(rnd_hex[i*2: i*2+2]),


