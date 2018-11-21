#!/usr/bin/env python

'''
Takes system input and returns each word in a Key Value Pair
The Key is the word sorted lexicographically (alphabetically), the Value is the original word
'''

import sys
import re


'''
This function takes input of each individual word, and returns true if that word is, or contains a number
This function is used to emit numbers, or words containing numbers from the output later
'''
def checkNum(inputString):
        return any(char.isdigit() for char in inputString)

for line in sys.stdin:

    #Call lower to make word lowercase
    #Use RegEx to remove any symbol that is not a number or letter and replace with a space
    lower_removePunct = re.sub(r"[^a-z0-9']", " ", line.lower())

    #seprates line into a list of words
    words = lower_removePunct.split()

    for word in words:

        #Call checkNum to see if the word is or contains any number(s),
        #Word only gets considered if it doesn't contain numbers
        if checkNum(word) is False:

            #If the word doesn't contain any numbers
            #Removes apostrophe
            noApost = re.sub(r"'","", word)

            # sorted_word is the word sorted lexicographically
            sorted_word = "".join(sorted(list(noApost)))

            #output the lexicographically sorted word and the word, separated by a tab
            print((sorted_word+'\t'+noApost))
