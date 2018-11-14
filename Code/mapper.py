#!/usr/bin/env python

# Takes input in form of text file and outputs list of key pairs
# Key is word sorted lexicographically
# Value is word

import string
import sys

punctuation = set(string.punctuation)

word_pairs = []

for line in sys.stdin:
    remove_punct = ''.join(x for x in line if x not in punctuation)
    line_no_punct = remove_punct.split()

    for word in line_no_punct:
        lower_word = word.lower()
        sorted_word = "".join(sorted(list(lower_word)))
        word_pairs.append((sorted_word+'\t'+lower_word))
        print((sorted_word+'\t'+lower_word))