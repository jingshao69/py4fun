#!/usr/bin/env python3

from scipy import stats
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('data_file')

args = parser.parse_args()

x=[]
y=[]

with open(args.data_file, 'r') as f:
   for line in f:
       data = line.rstrip().split(' ')
       if len(data) == 2:
           x.append(float(data[0]))
           y.append(float(data[1]))

   if len(x) != 0:
       slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
       print(" y = %.2f *x + %.2f" %(slope, intercept))
       print(" r = %.2f p = %.2f stderr = %.2f" %(r_value, p_value, std_err))

       


