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
def lower_removePunct(inputString):
    return  re.sub(r"[^a-z0-9']", " ", inputString.lower())

def wordList(inputString):
    return inputString.split()

def checkNum(inputString):
    return any(char.isdigit() for char in inputString)

def removeApost(inputString):
    return re.sub(r"'","", inputString)

def sortWord(inputString):
    return "".join(sorted(list(inputString)))

def printTest(sorted_word, word):
    return print((sorted_word+'\t'+word))
