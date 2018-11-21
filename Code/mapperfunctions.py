#!/usr/bin/env python

import sys
import re


'''
I have written unit tests for each function and provided more in-depth information in the "test_map" code I have also attached.
'''
'''
Function removes any punctuation, except apostrophes, from the lines input and replaces them with a space
'''
def lower_removePunct(inputString):
    return  re.sub(r"[^a-z0-9']", " ", inputString.lower())

'''
Function outputs a list of the individual words on each line
'''
def wordList(inputString):
    return inputString.split()
'''
Function returns true if there are numbers in the words passed
'''
def checkNum(inputString):
    return any(char.isdigit() for char in inputString)
'''
Function removes apostrophes but does not replace with spaces, so the characters, either side are concatenated
'''
def removeApost(inputString):
    return re.sub(r"'","", inputString)

'''
Function sorts the words input lexicographically (alphabetically)
'''
def sortWord(inputString):
    return "".join(sorted(list(inputString)))
'''
Below is where all of the code is executed. 
Every line passed through as input is made lower case and has most punctuation remove, 
Each word is then checked to see if there is a number or not, if not (checkNum returns False), 
The word is sorted lexicographically, and output as the Key in a Key-Value pair, with the Value being the original word
'''

for line in sys.stdin:
    lower_noPunct = lower_removePunct(line)
    word_List = wordList(lower_noPunct)

    for word in word_List:
        if checkNum(word) is False:
            no_Apost = removeApost(word)
            sorted_word = sortWord(no_Apost)
            print (sorted_word+'\t'+no_Apost)