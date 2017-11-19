#!/usr/bin/python

import argparse
import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

TIMEOUT=20

ENDP="https://api.iextrading.com/1.0"

def https_get_json(url):
    r = requests.get(url, verify=False, timeout=TIMEOUT)
    return r.json()

parser = argparse.ArgumentParser()
parser.add_argument('stock')

args = parser.parse_args()

url = ENDP + "/stock/" + args.stock + "/quote"
stock_data = https_get_json(url)

market_cap = stock_data['marketCap']/float(1000000000)
print "%s %s %s %.1fB" %(args.stock.upper(), stock_data['latestPrice'], stock_data['change'], market_cap)
