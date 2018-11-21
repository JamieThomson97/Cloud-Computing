import unittest
import dummyMap

class TestMap(unittest.TestCase):

#lower_removePunct is the first operation the input is passed through
#It takes lines of Strings. The strings can contain any character
#lower_removePunct should output the text with only lowercase letters, any numbers, and apostrophes, separated by spaces/tabs
    def test_lower_removePunct(self):
        self.assertEqual(dummyMap.lower_removePunct("FOOPAA"), "foopaa")
        self.assertEqual(dummyMap.lower_removePunct("FO!2£opa!a"), "fo 2 opa a")
        self.assertEqual(dummyMap.lower_removePunct("FOO paa"), "foo paa")

#The output of lower_removePunct is then passed to a split function.
#The input is lines of Strings of only lowercase letters, any numbers, and apostrophes, separated by spaces/tabs
#The function should output a list of the individual words, with numbers and apostrophes remaining
    def test_wordList(self):

        self.assertEqual(dummyMap.wordList("foo paa zee"), ["foo", "paa", "zee"])
        self.assertEqual(dummyMap.wordList("fo39o pa'a z1ee"), ["fo39o", "pa'a", "z1ee"])
        self.assertEqual(dummyMap.wordList("    "), [])



#The output is then passed to the checkNum function.
#The input can only be individual words with lowercase letters, numbers and apostrophes
#checkNum should return True if the word contains one or more number, false otherwise
    def test_checkNum(self):

        self.assertEqual(dummyMap.checkNum("foopaa"), False)
        self.assertEqual(dummyMap.checkNum(""), False)
        self.assertEqual(dummyMap.checkNum("99992349"), True)
        self.assertEqual(dummyMap.checkNum("f00p44"), True)
        self.assertEqual(dummyMap.checkNum("f0'p44"), True)
        self.assertEqual(dummyMap.checkNum("foopaa"), False)

#If the checkNum function returns False
#The individual words is then passed to an operation removing the apostrohpe
#The input can only be words containing lowercase letters and apostrophes
#removeApost should output the words with apostrophes removed
    def test_removeApost(self):

        self.assertEqual(dummyMap.removeApost("f'o'o'p'a'a"), "foopaa")
        self.assertEqual(dummyMap.removeApost("foopaa"), "foopaa")
        self.assertEqual(dummyMap.removeApost("foopaa'"), "foopaa")
        self.assertEqual(dummyMap.removeApost("'"), "")

#The word is then passed to a sorting function
#The input can be individual words, only containing letters
#The output should be the word sorted lexicographically
    def test_sortWord(self):

        self.assertEqual(dummyMap.sortWord("foopaa"), "aafoop")
        self.assertEqual(dummyMap.sortWord("abcdef"), "abcdef")
        self.assertEqual(dummyMap.sortWord("zyxwvut"), "tuvwxyz")