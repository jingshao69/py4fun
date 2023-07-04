#!/usr/bin/env python3

import sys
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

total_area = 0
init_printing(use_unicode=False, wrap_line = False)

x = Symbol('x')

def find_zero(F):
    result=solve(F)
    #print("%r: %r" %(F, result))
    return result

def area(F, r0, r1):
    a=simplify(integrate(F, (x, r0, r1)))
    return abs(a)

def get_func_val(x, isF1):
    #print "**%r %r**" %(x, isF1)
    if isF1:
        v1 = Function_F1(x)
        v2 = Function_F2(x)
    else:
        v1 = Function_F2(x)
        v2 = Function_F1(x)

    return v1,v2

def get_factor(x, isF1):
    (f1Val, f2Val) = get_func_val(x,isF1)
    #print f1Val, f2Val
    if (f1Val > 0) and (f2Val > 0) and (f1Val < f2Val):
        factor = -1
    elif (f1Val < 0) and (f2Val < 0) and (f1Val > f2Val):
        factor = -1
    else:
        factor = 1
    return factor


def find_sub_area(F, isF1, xranges):
    global total_area
    last_x_flag = False;
    min_x=xranges[0]
    max_x = xranges[1]

    F_zeros=find_zero(F)
    
    print("Function: %r zeros: %r\n" %(F, F_zeros))
    
    last_x = min_x

    end_x = max_x
    for x in F_zeros:
        if (x > min_x) and ( x <max_x):
            a = area(F, last_x, x)
            check_x = float((last_x +x)/2)

            factor = get_factor(check_x, isF1)

            total_area += a*factor
            #F_Func=lambdify(x, F)
            #print F_Func(check_x)

            last_x = x
            print("[%r - %r]: %r %r" %(last_x, x, a, factor))

    
    a = area(F, last_x, max_x)
    check_x = float((last_x +max_x)/2)
    factor = get_factor(check_x, isF1)

    total_area += a*factor
    print("[%r - %r]: %r %r\n" %(last_x, max_x, a, factor))
   

function = input("Enter your first function: ")

F1 = parse_expr(function, evaluate=False)
Function_F1=lambdify(x, F1)

function = input("Enter your second function: ")

F2 = parse_expr(function, evaluate=False)
Function_F2=lambdify(x, F2)

print("")
xranges= find_zero(F1-F2)
print("\nRange: [%r - %r]\n" %(xranges[0], xranges[1]))

find_sub_area(F1, True, xranges)

find_sub_area(F2, False, xranges)

print("Total Area: %r" %(total_area))

         
