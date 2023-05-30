
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter



x = list() # ships
y = list() # missiles
with open("ResultsSPathBinMC.txt", "r") as minfile:
    lines = minfile.readlines()
    for line in lines:
        vals = line.split(", ")
        x.append(int(vals[0]))
        y.append(int(vals[1]))

#x = np.array(xmin)
#y = np.array(ymin)

c = Counter(zip(x,y))
# create a list of the sizes, here multiplied by 10 for scale
s = [2*c[(xx,yy)] for xx,yy in zip(x,y)]


print(c)


#plt.scatter(x, y, s=s)
#plt.show()
