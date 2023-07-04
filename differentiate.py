#!/usr/bin/env python3

from sympy import * 
from sympy.parsing.sympy_parser import parse_expr

init_printing(use_unicode=False, wrap_line = False)

x = Symbol('x')

# Define the function write here
function_expr = input("Enter your Function: ")

F = parse_expr(function_expr, evaluate=False)

#F = x*sin(x)

F1 = diff(F, x)
F2 = diff(F1, x)

print("")

print("F' = %r" %(F1))
print("F'' = %r" %(F2))

