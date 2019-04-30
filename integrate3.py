#!/usr/bin/python

import sys
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

init_printing(use_unicode=False, wrap_line = False)

x = Symbol('x')

def find_zero(F):
    result=solve(F)
    #print "%r: %r" %(F, result)
    return result

def area(F, r0, r1):
    a=simplify(integrate(F, (x, r0, r1)))
    return abs(a)

def find_sub_area(F, xranges):
    last_x_flag = False;
    min_x=xranges[0]
    max_x = xranges[1]

    F_zeros=find_zero(F)
    
    print "Function: %r zeros: %r\n" %(F, F_zeros)
    
    start_x = last_x = min_x

    end_x = max_x
    for x in F_zeros:
        if (x > min_x) and ( x <max_x):
            a = area(F, start_x, x)
            last_x = x
            print "[%r - %r]: %r" %(start_x, x, a)

    
    a = area(F, last_x, max_x)
    print "[%r - %r]: %r\n" %(last_x, max_x, a)
   

function1 = raw_input("Enter your first function: ")

F1 = parse_expr(function1, evaluate=False)

function = raw_input("Enter your second function: ")

F2 = parse_expr(function, evaluate=False)

print ""
xranges= find_zero(F1-F2)
print "\nRange: [%r - %r]\n" %(xranges[0], xranges[1])

find_sub_area(F1, xranges)

find_sub_area(F2, xranges)

         
