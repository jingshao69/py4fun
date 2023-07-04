#!/usr/bin/env python3

import argparse
import myssh

parser = argparse.ArgumentParser()
parser.add_argument('--user', '-u', default=myssh.my_user, help='User Name')
parser.add_argument('--password', '-p', default=myssh.my_password, help='Password')
parser.add_argument('ip_addr')
parser.add_argument('cmd', nargs='+')

args = parser.parse_args()

ip_addr = args.ip_addr;
total_cmd = ' '.join(args.cmd)

myssh.initSSHPass()
myssh.execSSHCommand(ip_addr, total_cmd)
