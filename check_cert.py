#!/usr/bin/python

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

def check_cert(ip_addr):
    cert_data = {}
    algo_cnt=0
    token_array=("Issuer", "Subject", "Signature Algorithm", "Not Before", "Not After ", "Public-Key")
    cmd = 'echo | ' + get_openssl()+ ' s_client -showcerts -servername ' + ip_addr + ' -connect ' + ip_addr + ':443 2>' + get_null_file() +' | ' + get_openssl() + ' x509 -noout -text'
    #print(cmd)
    result = execCommand(cmd)
    #print(result)
    data = result.splitlines()

    for line in data:
        for token in token_array:
            index = line.find(token)
            if (index >= 0):
                value = line[index+len(token)+1:].replace("(","").replace(")","").lstrip().rstrip();

                if token == "Subject":
	            index2 = line.find("C=")
	            if index2 >= 0:
                        cert_data[token] = value
                        print("%s = %s" %(token, value))
                elif token == "Signature Algorithm":
	            if algo_cnt == 0:
                        cert_data[token] = value
                        print("%s = %s" %(token, value))
	                algo_cnt = 1

                else:
                    cert_data[token] = value
                    print("%s = %s" %(token, value))

    return cert_data

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('ip_addr')

  args = parser.parse_args()

  check_cert(args.ip_addr)




