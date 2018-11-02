# Takes the input as file, where each line a key value pair of a lexicographically sorted word as the key, and the actual word as the value
# Outputs a list of every occurrence every anagram in the input

import re

filename = "Dict2.txt"
fileopen = open(filename, 'r')

answer = {}

i = 0
with open(filename) as file:
    for line in file:
        comma_index = line.find(",")
        key = str(line)[2:(comma_index-1)]
        #print(value)
        value = str(line)[(comma_index+3):(len(str(line))-3)]
        if key not in answer:
            answer[key] = []

        answer[key].append(value)

for i in answer:
    if len(answer[i]) > 1:

        print (answer[i])
