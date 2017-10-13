#!/usr/bin/python

import paramiko
import argparse
from ssh_env import *

#Content of ssh_env.py
#my_user="user"
#my_password="password"


def execSSHCommand(ip_addr, cmd):
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh.connect(ip_addr, username=my_user, password=my_password)
  ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
  data = ssh_stdout.read().splitlines()
  for line in data:
    print line

parser = argparse.ArgumentParser()
parser.add_argument('--user', '-u', default=my_user, help='User Name')
parser.add_argument('--password', '-p', default=my_password, help='Password')
parser.add_argument('ip_addr')
parser.add_argument('cmd', nargs='+')

args = parser.parse_args()

ip_addr = args.ip_addr;
total_cmd = ' '.join(args.cmd)

execSSHCommand(ip_addr, total_cmd)
