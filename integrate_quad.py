#!/usr/bin/env python3

from math import *
import scipy.integrate as integrate
import func

minStr = raw_input("Enter min: ")
maxStr = raw_input("Enter max: ")

minVal = float(minStr)
maxVal = float(maxStr)

result= integrate.quad(func.F, minVal,maxVal)
print "F: \t%r" %(result[0])

