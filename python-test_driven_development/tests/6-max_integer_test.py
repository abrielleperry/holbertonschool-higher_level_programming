#!/usr/bin/Python3
"""unicode for max_function that returns max int from list"""


import unittest
max_integer = __import__('6-max_integer').max_integer
import pycodestyle

class TestMaxInteger(unittest.TestCase):
    """unitest for max_int function"""
    
    def test_correct_use(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        # 
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        #
        self.assertEqual(max_integer([1, 5, 10, 4, 8]), 10)
        #
        self.assertEqual(max_integer([7]), 7)
        #
        self.assertIsNone(max_integer())
        
    def test_incorrect_use(self):
        self.assertRaises(TypeError, max_integer((1, 2, 3)))
        #
        self.assertNotEqual(max_integer([]), 6)
        #
        #
        
        