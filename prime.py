#!/usr/bin/env python3


import math
import argparse

prime_array = [2,3,5,7]
prime_suffix = [1, 3, 7, 9]

def is_prime(x):
  max_factor= math.floor(math.sqrt(x))
  for prime in prime_array:
    if prime >max_factor:
      return 1
    if (x % prime) == 0:
      return 0

def add_prime(y):
  prime_array.append(y)    

def print_prime():
  cnt=0
  for prime in prime_array:
    if (cnt % PRIME_PER_LINE) == 0:
      print("%d" %(prime), end='')
    elif (cnt % PRIME_PER_LINE) == (PRIME_PER_LINE -1):
      print("\t%d\n" %(prime), end='')
    else:
      print("\t%d" %(prime), end='')
    cnt = cnt + 1
  print('')

parser = argparse.ArgumentParser()
parser.add_argument("--max", "-m", type=int, default=10000)
parser.add_argument("--col", "-c", type=int, default=10)
args = parser.parse_args()

PRIME_PER_LINE= args.col

for i in range(1, int(args.max/10)):
  for suffix in prime_suffix:
    num = i*10 + suffix
    if is_prime(num):
      add_prime(num)

print_prime()



