#!/usr/bin/env python

'''
Takes system input and returns each word in a Key Value Pair
The Key is the word sorted lexicographically (alphabetically), the Value is the original word
'''

import sys
import re


'''
This function takes input of each individual word, and returns true if that word is a number, or contains a number
This function is used to emit numbers or words containing numbers from the output later
'''
def checkNum(inputString):
        return any(char.isdigit() for char in inputString)


'''
Removes any punctuation(bar the apostrophe (')) and replaces it with a space. 
This is so punctuation isn't added to a word's Key and considered in the anagram matching. 
Also makes words lower case so words with capitals can match with words that do not
'''
def lower_removePunct(inputString):
    punct_removed_lower = re.sub(r"[^a-z0-9']", " ", inputString.lower())
    return  punct_removed_lower

for line in sys.stdin:

    #Call lower_removePunct to remove any punctuation, and make word lowercase
    remove_punct = lower_removePunct(line)
    #seprates line into a list of words
    words = remove_punct.split()

    for word in words:
        #Call checkNum to see if the word is or contains any number(s)
        if checkNum(word) is False:

            #If the word doesn't contain any numbers
            #Removes apostrophe
            noApost = re.sub(r"'","", word)
            # sorted_word is the word sorted lexicographically
            sorted_word = "".join(sorted(list(noApost)))
            #output the lexicographically sorted word and the word, separated by a tab
            print((sorted_word+'\t'+noApost))
