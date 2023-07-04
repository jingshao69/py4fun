#!/usr/bin/env python3

import sys
import argparse
import subprocess

OPENSSL="openssl"

def get_null_file():
  if sys.platform == 'win32':
    return 'nul'
  else:
    return '/dev/null'

def get_openssl():
  return OPENSSL

def execCommand(cmd):
  proc = subprocess.Popen(cmd, stdout = subprocess.PIPE, shell=True)
  (out, err) = proc.communicate()
  return out

def check_cipher(ip_addr):
    token_array=("Protocol ", "Cipher  ")
    cipher_data = {}
    cmd = 'echo | ' + get_openssl() + ' s_client -showcerts -servername ' + ip_addr + ' -connect ' + ip_addr + ':443 2> ' + get_null_file()
    #print(cmd)
    result = execCommand(cmd)
    #print(result)
    data = result.splitlines()

    for line in data:
        for token in token_array:
            index = line.find(token)
            if index >= 0:
                newtoken = token.lstrip().rstrip()
                value = line[index+len(token):].replace(":","").lstrip().rstrip()
                cipher_data[newtoken] = value
                print("%s = %s" %(newtoken, value))

    
    return cipher_data


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('ip_addr')

  args = parser.parse_args()

  check_cipher(args.ip_addr)




