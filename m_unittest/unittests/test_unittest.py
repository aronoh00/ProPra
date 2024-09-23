import unittest
import math


class TestStringMethods(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)


class TestMathMethods(unittest.TestCase):    
    def test_sqrt(self):
        self.assertAlmostEqual(math.sqrt(10)**2, 10, places=4)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            math.sqrt(-1)
