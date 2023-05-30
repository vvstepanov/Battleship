# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 14:28:18 2022

@author: VStep
"""

shipslist = list(range(20))#list()

for i in range(len(shipslist)):
    shipslist[i] = 0


with open("ResultsSPathATMC.txt", "r") as minfile:
    lines = minfile.readlines()
    for line in lines:
        vals = line.split(", ")
        count = int(vals[0])
        #print(count)
        shipslist[count] +=1


print(shipslist)
