# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 15:04:22 2021

@author: vs2018
"""

import os
import time
from tqdm import tqdm
import numpy as np
#import subprocess


# load files, min and max
rmin = list()
with open("Scenario.txt", "r") as minfile:
    lines = minfile.readlines()
    for line in lines:
        rmin.append(float(line))


rmax = list()
with open("ScenarioM.txt", "r") as maxfile:
    lines = maxfile.readlines()
    for line in lines:
        rmax.append(float(line))

minfile.close()
maxfile.close()
#print(rmin)
#print ("\n")
#print(len(rmin))

# permute 
permutations = list()
#permutations.append(rmin)
temp = 0
for i in range(60):
    xtest2 = list()
    for k in range(60):
        xtest2.append(rmin[k])

    for j in range(60-i):
        temp = rmax[j+i]
        xtest2[j+i] = temp
        # save list to list
        permutations.append(xtest2)

print("Scenarios generated")
print(len((permutations)))
#print(permutations[1829])
print ("\n")
#print(permutations[1830])

# launch py file x times with  radar permuation


# for radars in tqdm(range(len(permutations))):
#     with open("Testing.txt","w") as myfile:
#         myfile.seek(0)
#         for p in range(60):
#             myfile.write(str(permutations[radars][p]) + "\n")
#     myfile.close()
#     time.sleep(1)
#     os.system("python vladimirImpreciseABMBruteCMClean.py")



# #mc
rng = np.random.default_rng(220)
rU = list(range(60))
for s in range(60):
    rU[s] = rng.uniform(rmin[s], rmax[s],1830)

for t in tqdm(range(1830)):
    # Nradars = list(range(60))
    # for s in range(60):
    #     Nradars[s] = rU[s][t]
    # # print(Nradars)
    # # print("NEWline" + "/n")
    with open("Testing.txt","w") as myfile:
        myfile.seek(0)
        for p in range(60):
            #print(str(rU[p][t]))
            myfile.write(str(rU[p][t]) + "\n")
    myfile.close()
    time.sleep(1)
    os.system("python vladimirImpreciseABMBruteCMClean.py")
