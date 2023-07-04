#!/usr/bin/env python3

import io

battle_dict={}
ship_cnt=0

with io.open("IJNCarrier.txt", "r", encoding='utf8') as f:
    for line in f:
        fields=line.strip().split(":")
        if len(fields) == 2:
            battle=fields[1]
            if battle in battle_dict.keys():
                 #print "%s %s" %(battle, fields[0])
                 battle_dict[battle].append(fields[0])
            else:
                 ships = [fields[0]]
                 battle_dict[battle] = ships
            #print fields[0], fields[1]

for battle in battle_dict.keys():
    if battle != "Scrapped":
        print("%s:\t%d" %(battle, len(battle_dict[battle])))
        ship_cnt += len(battle_dict[battle])
        for s in battle_dict[battle]:
            print("\t%s" %(s),end='')
        print("")

print("\nTotal:\t%d" %(ship_cnt))


        


