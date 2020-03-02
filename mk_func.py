#!/usr/bin/python

expr = raw_input("Please enter expression: ")
body = '    return (' + expr + ')'

with open('func.py', 'w') as f:

    f.write('#!/usr/bin/python\n')
    f.write('import math\n\n')
    f.write('def F(x):\n')
   
    f.write(body)

