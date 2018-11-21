
import unittest
#import test_reduce
import dummyMap

class TestMap(unittest.TestCase):

    def test_checkNum(self):

        self.assertEqual(dummyMap.checkNum("Jamie"), False)
        self.assertEqual(dummyMap.checkNum(""), False)
        self.assertEqual(dummyMap.checkNum("99992349"), True)
        self.assertEqual(dummyMap.checkNum("J4m1e"), True)