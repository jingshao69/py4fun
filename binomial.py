#!/usr/bin/env python3

import math
import argparse

def factorial(n):
    result=1
    for i in range(1, n+1):
        result *= i
    return result

def binomial(n, k):
    return math.factorial(n) / (math.factorial(n-k) * math.factorial(k))

parser = argparse.ArgumentParser()
parser.add_argument('n')
parser.add_argument('k')
parser.add_argument('p')

args = parser.parse_args()

nn=int(args.n)
kk=int(args.k)
pp=float(args.p)


print("%.3f" %(binomial(nn, kk) *math.pow(pp,kk)*math.pow(1-pp, nn-kk)))

