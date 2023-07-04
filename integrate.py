#!/usr/bin/env python3

from sympy import * 
from sympy.parsing.sympy_parser import parse_expr

init_printing(use_unicode=False, wrap_line = False)

x = Symbol('x')

# Define the function write here
function_expr = input("Enter your Function: ")

F = parse_expr(function_expr, evaluate=False)

print("%r" %(F))

G = integrate(F, x)

print("%r" %(G))

