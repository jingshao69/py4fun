#!/usr/bin/python

import argparse

FED_TAX_RATES_OLD=[0.10, 0.15, 0.25, 0.28, 0.33, 0.35, 0.396]

FED_TAX_LIMITS_OLD = [ 18650, 75900, 153100, 233350, 416700, 470700, 10000000000 ]

FED_TAX_RATES_NEW=[0.10, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]

FED_TAX_LIMITS_NEW = [ 19050, 77400, 165000, 315000, 400000, 600000, 10000000000 ]

def get_fed_tax(total_income, new):
   if new == 0:
       FED_TAX_RATES=FED_TAX_RATES_OLD
       FED_TAX_LIMITS=FED_TAX_LIMITS_OLD
   else:
       FED_TAX_RATES=FED_TAX_RATES_NEW
       FED_TAX_LIMITS=FED_TAX_LIMITS_NEW
     
   fed_taxable = total_income 

   num_bracket = len(FED_TAX_RATES)
   fed_tax = 0.0
   lower_limit = 0.0
   for i in range(0, num_bracket):
     if fed_taxable < FED_TAX_LIMITS[i]:
       fed_tax = fed_tax + (fed_taxable - lower_limit) * FED_TAX_RATES[i]
       return fed_tax
     else:
       fed_tax = fed_tax + (FED_TAX_LIMITS[i] - lower_limit) * FED_TAX_RATES[i]
       #print fed_tax
       lower_limit = FED_TAX_LIMITS[i]


parser = argparse.ArgumentParser()
parser.add_argument('old_taxable')
parser.add_argument('new_taxable')

args = parser.parse_args()

old_tax = get_fed_tax(int(args.old_taxable), 0)
new_tax = get_fed_tax(int(args.new_taxable), 1)

print "2017: %d 2018: %d Delta: %d" %(old_tax, new_tax, new_tax - old_tax)



