#Script to split Dict.txt into 2 files, by alternating lines

FileName = "dict.txt"

with open(FileName) as f:
    FileName1 = "Dict1.txt"
    FileName2 = "Dict2.txt"
    FileOpen1 = open(FileName1, "w")
    FileOpen2 = open(FileName2, "w")
    i = 0
    for line in f.readlines():
        word = line.strip()
        if (i % 2 == 0):
            FileOpen1.write(word + '\n')
        if (i % 2 != 0):

            FileOpen2.write(word + '\n')
        i += 1

    FileOpen1.close()
    FileOpen2.close()


