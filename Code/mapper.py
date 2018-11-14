# Takes input in form of text file and outputs list of key pairs
# Key is word sorted lexicographically
# Value is word

import string
import sys
FileName = "dict.txt"
count = 0
punctuation = set(string.punctuation)


def make_list():
    word_pairs = []
    for line in sys.stdin.readlines():
        remove_punct = ''.join(x for x in line if x not in punctuation)
        line_no_punct = remove_punct.split()

        for word in line_no_punct:
            lower_word = word.lower()
            sorted_word = "".join(sorted(list(lower_word)))
            word_pairs.append((sorted_word+'\t'+lower_word))
            print((sorted_word+'\t'+lower_word))
            #print(sorted_word, "\t", lower_word)
    return word_pairs


result = make_list()

#print(result)

i = 0

FileName1 = "Dict1.txt"
FileName2 = "Dict2.txt"
FileOpen1 = open(FileName1, "w")
FileOpen2 = open(FileName2, "w")


for line in result:

    if i % 2 == 0:
        # print ("in even")
        FileOpen1.write(str(line)+"\n")

    if i % 2 != 0:
        # print("in odd")
        FileOpen2.write(str(line)+"\n")

    i += 1

FileOpen1.close()
FileOpen2.close()


