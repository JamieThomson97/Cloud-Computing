# Takes input in form of text file and outputs list of key pairs
# Key is word sorted lexicographically
# Value is word

FileName = "dict.txt"


def make_list(file):
    word_pairs = []
    with open(file) as f:
        for line in f.readlines():
            word = line.strip()
            sorted_word = "".join(sorted(list(word)))
            word_pairs.append((sorted_word, word))
    return word_pairs


result = make_list(FileName)
test = result[1000]

print(test)

i = 0

FileName1 = "Dict1.txt"
FileName2 = "Dict2.txt"
FileOpen1 = open(FileName1, "w")
FileOpen2 = open(FileName2, "w")

for line in result:

    if i % 2 == 0:
        # print ("in even")
        FileOpen1.write(str(line))
    if i % 2 != 0:
        # print("in odd")
        FileOpen2.write(str(line))
    i += 1

FileOpen1.close()
FileOpen2.close()


