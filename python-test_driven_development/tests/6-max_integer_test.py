#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        """Test max_integer function"""
        # Test with a list of positive integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        # Test with a list of positive integers in a different order
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        # Test with a list of negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        # Test with a list of mixed positive and negative integers
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        # Test with an empty list
        self.assertEqual(max_integer([]), None)
        # Test with a list containing only one element
        self.assertEqual(max_integer([5]), 5)

if __name__ == '__main__':
    unittest.main()
