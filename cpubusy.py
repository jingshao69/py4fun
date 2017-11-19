#!/usr/bin/python

import re
import time

idle=[]
total=[]

def getCpuInfo():
    cpu_num = 0
    cpu_model = ""
    with open('/proc/cpuinfo') as f:
        for line in f:
            if(re.match("^model name", line)):
		if (cpu_model == ""):
	        	cpu_model = line.split(":")[1].strip()
                cpu_num += 1
    return cpu_model, cpu_num

def getMemInfo():
    with open('/proc/meminfo') as f:
        for line in f:
	    fields=line.strip().split(":")
            if(re.match("MemTotal", fields[0])):
                mem_kb = fields[1].replace("kB", "")
	        total_mem = int(mem_kb)/1024
            if(re.match("HugePages_Total", fields[0])):
	        total_hugepages= int(fields[1])
    return total_mem

cpu_model, numCPU = getCpuInfo()
total_mem = getMemInfo()
print "CPU:      %s" %(cpu_model)
print "NumCPU:   %d" %(numCPU)
print "MemTotal: %d MB" %(total_mem)



idle = [0] * numCPU
total = [0] * numCPU
last_idle = [0] * numCPU
last_total = [0] * numCPU

while True:
    with open('/proc/stat') as f:
        for line in f:
            if(re.match("^cpu", line)):
                fields = line.strip().split()
		if (fields[0] != "cpu" ):
                    cpu_id = int(fields[0][3:]) 
                    idle[cpu_id] = float(fields[4])
                    total[cpu_id] = 0.0
		    for data in fields[1:]:
                        total[cpu_id] += float(data) 
                    idle_delta, total_delta = idle[cpu_id] - last_idle[cpu_id], total[cpu_id] - last_total[cpu_id]
                    last_idle[cpu_id], last_total[cpu_id] = idle[cpu_id], total[cpu_id]
                    utilisation = 100.0 * (1.0 - idle_delta / total_delta)
                    print '%d %5.1f%%' %(cpu_id, utilisation)
    time.sleep(5)
