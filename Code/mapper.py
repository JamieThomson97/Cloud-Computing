#!/usr/bin/env python

# Takes input in form of text file and outputs list of key pairs
# Key is word sorted lexicographically
# Value is word

import sys
import re

def hasNumbers(inputString):
        return any(char.isdigit() for char in inputString)


for line in sys.stdin:
    remove_punct = re.sub(r"[,.;@#?!&$\":/'()\[\]*'-]+\ *", " ", line)
    line_no_punct = remove_punct.split()

    for word in line_no_punct:
        if hasNumbers(word) is False:
            lower_word = word.lower()
            sorted_word = "".join(sorted(list(lower_word)))
            print((sorted_word+'\t'+lower_word))