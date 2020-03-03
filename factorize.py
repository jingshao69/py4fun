#!/usr/bin/python

import math
import argparse

def find_factors(n):
    factors={}
    j = 2;
    while n > 1:
        n_sqrt = int(math.sqrt(n)) + 1;
        #print "n: %d j: %d n_sqrt: %d " %(n, j, n_sqrt)
        find_factor = False
        for i in xrange(j, n_sqrt):
            if n % i == 0:
                find_factor = True
                if i in factors.keys():
                    factors[i] += 1
                else:
                    factors[i] = 1

                n /= i  
                j = i
                break
        
        # If we can't find a factor, we should be done
        if not find_factor:
            if n > 1:
                if n in factors.keys():
                    factors[n] += 1
                else:
                    factors[n] = 1
            n /= n

    return factors
            
 
parser = argparse.ArgumentParser()
parser.add_argument('number', type=int)
args = parser.parse_args()

factors = find_factors(args.number)

print "%d = " %(args.number),
for key in sorted(factors):
   if factors[key] > 1:
       print "(%d)^%d" %(key, factors[key]),
   else:
       print "(%d)" %(key),


print ""


