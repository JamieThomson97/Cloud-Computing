#This script will take multiple inputs, produced from the mapper, and will add all the results together producing one master Dictionary

#Will Attempt first with 2 files

Master = {} #Final Dictionary

FileName1 = "Dict1.txt"
FileOpen1 = open(FileName1)

lineNo = 0
lines = FileOpen1.readlines()
for line in lines:
    if lineNo % 2 == 0: #is even
        if line.strip() not in Master:
            Master[line.strip()] = []
    #else:

    lineNo += 1

print (Master)