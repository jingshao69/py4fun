#!/usr/bin/python

from sympy import *

init_printing(use_unicode=False, wrap_line = False)

x = Symbol('x')

def area_vol(F,a, b):
  G = pi*F*F
  area = integrate(F, (x,a, b))
  volume = integrate(G, (x, a, b))
  print "Function: %r\tArea: %r\tVolume: %r " %(F, area, volume)


area_vol(sqrt(x), 0, 1)
area_vol(x, 0, 1)
area_vol(x**2, 0, 1)
area_vol(x**3, 0, 1)
area_vol(sin(Rational(1,2)*pi*x), 0, 1)
area_vol(cos(Rational(1,2)*pi*x), 0, 1)
