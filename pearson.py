#!/usr/bin/env python3

import math
import scipy.stats

array1=[1,2,3,4,5,6,7,8,9,10]

#array2=[2,4,6,8,10,12,14,16,18,20]

array2=[1,4,9,16,25,36,49,64,81,100]


def average(x):
    return float(sum(x)) / len(x)

def pearson_coeff(x, y):
    n = len(x)
    avg_x = average(x)
    avg_y = average(y)
    diffprod = 0
    xdiff2 = 0
    ydiff2 = 0
    for idx in range(n):
        xdiff = x[idx] - avg_x
        ydiff = y[idx] - avg_y
        diffprod += xdiff * ydiff
        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff

    return diffprod / math.sqrt(xdiff2 * ydiff2)

coeff, pvalue=scipy.stats.pearsonr(array1, array2)
coeff2 = pearson_coeff(array1, array2)

print(coeff)
print(coeff2)

