# Takes the input as file, where each line a key value pair of a lexicographically sorted word as the key, and the actual word as the value
# Outputs a list of every occurrence every anagram in the input


filename = "Dict1.txt"
fileopen = open(filename, 'r')

import sys
answer = {}

i = 0
with open(filename) as file:
    for line in sys.stdin:
        words = line.split("\t")
        key = words[0].strip("\r\n")
        #print(value)
        value = words[1].strip("\r\n")
        if key not in answer:
            answer[key] = []

        answer[key].append(value)


FileName1 = "Mapped.txt"

FileOpen1 = open(FileName1, "w")

for i in answer:
    if len(answer[i]) > 1:
        FileOpen1.write(str(answer[i])+"\n")
        print(str(answer[i])+"\n")


