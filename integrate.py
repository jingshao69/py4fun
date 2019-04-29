#!/usr/bin/python

from sympy import *

init_printing(use_unicode=False, wrap_line = False)

x = Symbol('x')

F1 = 12*x-2
F2 =  2*x**2+6*x-2

a = solve(F1)

print "%r: %r" %(F1, a)

result = solve(F2)

print "%r: %r" %(F2, result)

b = result[1]

c = solve(F1-F2)

print c

area1 = -simplify(integrate(F2, (x, 0, b)))
area2 = -integrate(F1,(x,0, a))

total_area1 = area1 - area2

print "***************"

print "area1: %r" %(area1)
print "area2: %r" %(area2)
print "total_area1: %r" %(total_area1)

area3 = integrate(F1, (x, a, 3))
area4 = simplify(integrate(F2, (x, b, 3)))

total_area2 = area3 - area4

print "area3: %r" %(area3)
print "area4: %r" %(area4)
print "total_area2: %r" %(total_area2)

print "total_area: %r" %(simplify(total_area1 + total_area2))

