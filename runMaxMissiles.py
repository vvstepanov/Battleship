
idslist = ""#list()
maxMissiles = 0

with open("ResultsSPathBinMC.txt", "r") as minfile:
    lines = minfile.readlines()
    for line in lines:
        vals = line.split(", ")
        count = int(vals[0])
        if (count != 0):
            temp = 0
            for i in range(count):
                #id: missiles -> need to get just missiles and add
                numMis = vals[i+1].split(":")
                temp += int(numMis[1])
            if (temp > maxMissiles):
                maxMissiles = temp
                idslist = line



print(maxMissiles)
print(idslist)
