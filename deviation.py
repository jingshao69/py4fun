#!/usr/bin/env python3

import numpy as np
import math


def average(array):
    return float(sum(array)/len(array))

def std_deviation(array):
    size = len(array)
    avg = average(array)
    ds_sum = 0.0
    for i in range(size):
       delta = array[i] - avg
       ds_sum += delta**2
    dev = math.sqrt(ds_sum/size)
    return dev


array = [1,2,3,4,5, 6, 7]

print(np.std(array))
print(std_deviation(array))

