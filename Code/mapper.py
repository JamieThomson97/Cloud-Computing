#This script takes a an input of words as a .txt file, and returns a dictionary
#The key's will be the words sorted lexicographically, values being being every occurrence of that anagram

FileName = "dict.txt" #A file containing thousands of random words

#Function separates each word into a dictionary the key being the word with value 1

def allWords(FileName):
    words = {}
    with open(FileName) as f:
            for line in f.readlines():
                word = line.strip()
                words[word] = 1
    return words

#Function returns a dictionary of every word sorted lexicographically, and the values are every permutation of said word that appears in the input

def findAnagrams(words):
    anagram_dict = {}
    for word in words:

            #Sorts current word lexicographically
            sortedWord = "".join(sorted(list(word)))
            #If this word is not already in the dictionary, add it
            if sortedWord not in anagram_dict:
                anagram_dict[sortedWord] = []
            #Append the current word(not sorted) to the set of values
            anagram_dict[sortedWord].append(word)
    return anagram_dict

#The above function returns every word, even if there is no anagram of it.
#So the below function returns a new dictionary containing only key-value pairs with more than one value
#I.E. more the sorted word has appeared more than once, so there must be an anagram of it

def Anagrams(anagrams_dict):
    result = {}

    for pair in anagrams_dict:
        No_of_Values = len(anagrams_dict[pair])
        KeyLength = len(pair)
        if No_of_Values > 1 and KeyLength > 2 :
            result[pair] = anagrams_dict[pair]
    return result

RunWords = allWords(FileName)
RunAnagrams = findAnagrams(RunWords)
FilterAnagrams = Anagrams(RunAnagrams)

for i in FilterAnagrams:
    print (i)
    print (FilterAnagrams[i])
    print ("")

#Attempt to write Result dictionary to a file

FileName = "Mapped.txt"
FileOpen = open(FileName, "w")

for Key, Value in FilterAnagrams.items():
    FileOpen.write(str(Key) + '\n\n'+ str(Value) + '\n\n\n\n')

FileOpen.close()
