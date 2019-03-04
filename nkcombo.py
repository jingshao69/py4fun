#!/usr/bin/python

import math
import argparse

def factorial(n):
    result=1
    for i in range(1, n+1):
        result *= i
    return result

def combo_n2k(n, k):
    num_combinations = math.factorial(n+k-1) / (math.factorial(n) * math.factorial(k-1))
    return num_combinations

parser = argparse.ArgumentParser()
parser.add_argument('n')
parser.add_argument('k')

args = parser.parse_args()

nn=int(args.n)
kk=int(args.k)

print "%d" %(combo_n2k(nn,kk))




