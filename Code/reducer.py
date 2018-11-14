#!/usr/bin/env python

# Takes the input as file, where each line a key value pair of a lexicographically sorted word as the key, and the actual word as the value
# Outputs a list of every occurrence every anagram in the input



import sys

anagram_pairs = {}


for line in sys.stdin:
    words = line.split("\t")

    key = words[0].strip("\r\n")
    value = words[1].strip("\r\n")

    if key not in anagram_pairs:
        anagram_pairs[key] = []
    if value not in [x for v in anagram_pairs.values() for x in v]:

        anagram_pairs[key].append(value)

i = 0

for i in anagram_pairs:
    if len(anagram_pairs[i]) > 1:
        print(str(anagram_pairs[i])+"\"\n")