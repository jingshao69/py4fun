#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("macAddr")

args = parser.parse_args()

PEN=34675

PEN |= 0x80000000
pen_str = hex(PEN)[2:]
mac_str = args.macAddr.replace(":", "").lower()

engine_str = pen_str + "03" + mac_str + "00"

print "%s" %(engine_str)

