#!/usr/bin/env python3

from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import argparse

init_printing(use_unicode=False, wrap_line = False)

x = Symbol('x')

def area_vol(F,a, b):
  G = pi*F*F
  area = integrate(F, (x,a, b))
  volume = integrate(G, (x, a, b))
  print("Function: %r\tArea: %r\tVolume: %r " %(F, area, volume))


parser = argparse.ArgumentParser()
parser.add_argument('func_desc_file')

args = parser.parse_args()

with open(args.func_desc_file, 'r') as f:
  for line in f:
    data = line.strip()
    if len(data) > 0:
      F = parse_expr(data, evaluate=False)
      area_vol(F, 0, 1)

