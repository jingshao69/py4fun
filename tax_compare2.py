#!/usr/bin/env python3

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
parser.add_argument('deduction_loss', type=int)
parser.add_argument('num_kids_under_17', type=int)
parser.add_argument('num_kids_over_17', type=int)

args = parser.parse_args()

min_income=50000
max_income=250000
income=min_income
while income <= max_income:
    old_taxable = income
    new_taxable = income + 4050 * (2 + args.num_kids_under_17 + args.num_kids_over_17) + args.deduction_loss
    old_tax = get_fed_tax(old_taxable, 0) - 1000 * args.num_kids_under_17 
    new_tax = get_fed_tax(new_taxable, 1) - 2000*args.num_kids_under_17 - 500 *args.num_kids_over_17

    print("2017: %d/%d 2018: %d/%d Delta: %d" %(old_tax, old_taxable, new_tax, new_taxable,new_tax - old_tax))
    income = income + 1000



