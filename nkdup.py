#!/usr/bin/python

import math
import argparse

def factorial(n):
    result=1
    for i in range(1, n+1):
        result *= i
    return result

def prob_dup_nk(n, k):
    total_choice = math.pow(n, k)
    non_dupl_choice = math.factorial(n) / math.factorial(n-k) 
    #print non_dupl_choice, total_choice
    prob = 1.0 - (non_dupl_choice * 1.0) / total_choice
    return prob

parser = argparse.ArgumentParser()
parser.add_argument('n')
parser.add_argument('k')

args = parser.parse_args()

nn=int(args.n)
kk=int(args.k)

if (kk > nn):
    print "1.000"
else:
    print "%.3f" %(prob_dup_nk(nn,kk))




