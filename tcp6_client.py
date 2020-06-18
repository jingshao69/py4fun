#!/usr/bin/python

import socket
import sys
import argparse

PORT = 8008

argparser = argparse.ArgumentParser()
argparser.add_argument('ip_addr')
args = argparser.parse_args()

HOST = args.ip_addr
#HOST = 'fd53:5043:5000:4732:5054:ff:fec9:605c'    # The remote host
#HOST = '10.71.50.175'

s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    #print res
    af, socktype, proto, canonname, sa = res
    try:
	s = socket.socket(af, socktype, proto)
    except socket.error, msg:
	s = None
	continue
    try:
	s.connect(sa)
    except socket.error, msg:
	s.close()
	s = None
	continue
    break

if s is None:
    print 'could not open socket'
    sys.exit(1)

Messages=["Hello World!", "Peace on Earth!", "Love Each Other!"]
for m in Messages:
    print 'Sent: %s' %(m)
    s.send(m)
    data = s.recv(1024)
    print 'Received %s' %(str(data))
