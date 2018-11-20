#!/usr/bin/env python

# Takes system input, where each line a key value pair of a lexicographically sorted word as the key, and the actual word as the value
# Outputs a list of every occurrence every anagram in the input


import sys

# Dictionary that the Key Value pairs will be added to
anagram_pairs = {}

for line in sys.stdin:

    # For every line input, separate the string on the "tab" character
    # This will produce a list containing the Key as element 0 and Value as element 1
    words = line.split("\t")

    # Assign the Key and the Value
    key = words[0].strip("\r\n")
    value = words[1].strip("\r\n")

    # If the Key (word sorted lexicographically) is not in the anagram_pairs dictionary,
    # i.e. hasn't appeared in the input yet,
    # Add the Key as a new Key in the anagram_pairs dictionary
    if key not in anagram_pairs:
        anagram_pairs[key] = []

    # If the Value is not already in the current Key's values,
    # e.g. this anagram of the current word, has not appeared in input yet
    # Add the Value to the Key's values
    if value not in anagram_pairs[key]:
        anagram_pairs[key].append(value)

# For every Key-Values set in anagram_pairs
for i in anagram_pairs:
    # If there is atleast 2 values in the values, i.e. atleast a pair of anagrams
   if len(anagram_pairs[i]) > 1:
       # Output the set of anagrams for that particular word
       print(str(anagram_pairs[i])+"\"\n")
