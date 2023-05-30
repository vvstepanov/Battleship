
idslist = list()

with open("ResultsRPathBinMC.txt", "r") as minfile:
    lines = minfile.readlines()
    for line in lines:
        vals = line.split(", ")
        count = int(vals[0])
        if (count != 0):
            for i in range(count):
                if (vals[i+1].strip("\n") not in idslist):
                    idslist.append(vals[i+1].strip("\n"))

print(idslist)
