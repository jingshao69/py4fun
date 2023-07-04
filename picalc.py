#!/usr/bin/env python3
# This is a python code to calculate Pi using the Machin-like formula
# Multiple threads are started to handle diffent parts of calulation

import argparse
from mpmath import mp
import threading

CA = ['183', '32', '-68', '12', '-100','-12', '12']
CB = ['239', '1023', '5832', '113021', '6826318', '33366019650', '43599522992503626068'] 


class CalcThread(threading.Thread):
  def __init__(self, threadID):
    threading.Thread.__init__(self)
    self.threadID = threadID

  def run(self):
    global pi
    A = mp.mpf(CA[self.threadID])
    B = mp.mpf(CB[self.threadID])
    sum = A * mp.atan(mp.mpf('1.0')/B)

    threadLock.acquire()
    pi = pi + mp.mpf('4.0') * sum
    threadLock.release()


parser = argparse.ArgumentParser()
parser.add_argument('--digits', '-d', type=int, default=10000)

args = parser.parse_args()

mp.dps = args.digits
pi =mp.mpf('0.0')

threadLock = threading.Lock()
threads = []

numThread = len(CA)
for i in range(0,numThread):
  thread = CalcThread(i)
  thread.start()
  threads.append(thread)

for t in threads:
  t.join()


print(pi)

