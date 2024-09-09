import unittest
import math


class TestStringMethods(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)


class TestMathMethods(unittest.TestCase):    
    @unittest.expectedFailure
    def test_sqrt(self):
        self.assertEqual(math.sqrt(10)**2, 10)
