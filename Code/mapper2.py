# Takes input in form of text file and outputs list of key pairs
# Key is word sorted lexicographically
# Value is word

import string
import sys
import re

FileName = "3314.txt"
count = 0
punctuation = set(string.punctuation)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def make_list(file):
    word_pairs = []
    with open(file) as f:
        for line in f.readlines():
            remove_punct = re.sub(r"[,.;@#?!&$\":/'()\[\]*'-]+\ *", " ", line)
            #print (remove_punct)
            line_no_punct = remove_punct.split()
            print (line_no_punct)
            for word in line_no_punct:
                if is_number(word) is False:
                    lower_word = word.lower()
                    sorted_word = "".join(sorted(list(lower_word)))
                    word_pairs.append((sorted_word+"\t"+lower_word))
                    #print(sorted_word, "\t", lower_word)
                else:
                    print ("")
    return word_pairs


result = make_list(FileName)

#print(result)

i = 0

FileName1 = "Dict1.txt"

FileOpen1 = open(FileName1, "w")


for line in result:

    FileOpen1.write(str(line)+"\n")

FileOpen1.close()



