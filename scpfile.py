#!/usr/bin/env python3

import myssh
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--user', '-u', default=myssh.my_user, help='User Name')
parser.add_argument('--password', '-p', default=myssh.my_password, help='Password')
parser.add_argument('--get', '-g', action='store_true')
parser.add_argument('ip_addr')
parser.add_argument('srcfile')
parser.add_argument('destfile')

args = parser.parse_args()

ip_addr = args.ip_addr;

myssh.initSSHPass()
scp = myssh.createSCPClient(ip_addr)

if (args.get):
  scp.get(args.srcfile, args.destfile)
else:
  scp.put(args.srcfile, args.destfile)

myssh.closeSCPClient(scp)
