import unittest
import mapper
import calc
import sys

class TestReduce(unittest.TestCase):

    def test_mapping(self):
        result = calc.add(1,2)
        self.assertEqual(result, 3)
