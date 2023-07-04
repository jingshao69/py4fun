#!/usr/bin/env python3

import time
import multiprocessing
import subprocess
import netaddr
import os
import sys
import argparse
import re
import socket, fcntl, struct
from netifaces import interfaces, ifaddresses, AF_INET

CONFIG_FILE= os.environ['HOME'] + "/.known_hosts"
MAC_ADDR_STR="MAC Address"
DEFAULT_NET="192.168.3.0"
OUI_MAP="oui.map"

my_ip=""

oui_map={}
mac_map={}
ip_list=[]
known_hosts = {}

def get_ouimap_file():
    if os.path.exists(OUI_MAP):
        return OUI_MAP

    bin_oui_map = os.environ['HOME'] + '/bin/' + OUI_MAP
    if os.path.exists(bin_oui_map):
        return bin_oui_map
    return ''

def pinger( job_q, results_q ):
    DEVNULL = open(os.devnull,'w')
    while True:
        ip = job_q.get()
        if ip is None: break

        try:
            subprocess.check_call(['ping','-c5',ip],
                                  stdout=DEVNULL)
            results_q.put(ip)
        except:
            pass

def init_oui_map():
    global oui_map
    oui_mapfile = get_ouimap_file()
    with open(oui_mapfile, "r") as ins:
        for line in ins:
            fields = line.split(":")
            mac = fields[0].strip()
            company = fields[1].strip()
            oui_map[mac]=company
    ins.close()

def get_company(oui):
    if oui in oui_map:
        return oui_map[oui]
    else:
        return ""

def get_oui(mac):
    new_oui=[]
    oui=mac[:8].replace(":","").encode('utf-8')
    ouiArray =  bytearray(oui)
    for i in range(len(ouiArray)):
        if ((ouiArray[i] >= ord('a')) and (ouiArray[i] <= ord('f'))):
           ouiArray[i] = ord('A') + ouiArray[i] - ord('a')

    return str(ouiArray)

def get_mac():
    global mac_map
    with open("/proc/net/arp", "r") as ins:
        for line in ins:
            fields = line.split()
            if len(fields) == 6:
                ip=fields[0]
                if (fields[3] != "00:00:00:00:00:00"):
                    mac_map[ip] = fields[3]
    ins.close()

def get_my_ip():
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
        if re.match("^e", ifaceName):
            return ifaceName, addresses[0]

def get_my_mac(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', str(ifname[:15])))
    #return ':'.join(['%02x' % ord(char) for char in info[18:24]])
    return ""

def init_my_ip():
    my_intf, my_ip=get_my_ip()
    my_mac_addr = get_my_mac(my_intf)
    print("Adding my own %s ==> %s to the Map" %(my_ip, my_mac_addr))
    mac_map[my_ip]=my_mac_addr

def do_ping(subnet):
    global ip_list
    pool_size = 255

    jobs = multiprocessing.Queue()
    results = multiprocessing.Queue()

    pool = [ multiprocessing.Process(target=pinger, args=(jobs,results))
             for i in range(pool_size) ]

    for p in pool:
        p.start()

    for i in range(1,255):
        ip_str = subnet + "." + str(i)
        jobs.put(ip_str)

    for p in pool:
        jobs.put(None)

    for p in pool:
        p.join()

    while not results.empty():
        ip = results.get()
        nip = netaddr.IPAddress(ip)
        ip_list.append(nip)

def load_know_hosts():
   global know_hosts

   if os.path.isfile(CONFIG_FILE):
      with open(CONFIG_FILE, "r") as fin:
          for line in fin:
              fields = line.strip().split("=")
              if len(fields) == 2:
                  mac= fields[0].lstrip().strip()
                  desc= fields[1].lstrip().strip()
                  known_hosts[mac] = desc

def print_desc(ip):
    if ip in mac_map:
        mac = mac_map[ip]
        if mac in known_hosts:
            print("%s ====> %s (%s)" %(ip, mac, known_hosts[mac]))
        else:
            oui = get_oui(mac)
            company = get_company(oui)
            print("%s ==> %s (%s)" %(ip, mac, company))

    else:
        print("%s not found in ARP table!" %(ip))

parser = argparse.ArgumentParser()
parser.add_argument('--net', '-n', default=DEFAULT_NET, help="Subnet")

args = parser.parse_args()

net_parts=args.net.split(".")

subnet=".".join(net_parts[:3])

if not os.path.exists("/proc/net/arp"):
    print("No /proc/net/arp found! Not a true Linux system!")
    sys.exit()

#Find my own IP/MAC and add to the map
init_my_ip()

print("[Scanning network %s.0...]" %(subnet))

do_ping(subnet)

print("[Scanning Complete]")

print("[Reading OUI Map...]")
init_oui_map()

time.sleep(1)
load_know_hosts()

print("[Reading ARP Table...]")
get_mac()
arp_ip_list=mac_map.keys()

ip_list.sort()
print("[Hosts responding to ping...]")
for ip in ip_list:
    ip_str = str(ip)
    print_desc(ip_str)

print("")
print("[Hosts not responding to ping but is in ARP table...]")
for ip in arp_ip_list:
    nip = netaddr.IPAddress(ip)
    if (nip not in ip_list):
        print_desc(ip)
