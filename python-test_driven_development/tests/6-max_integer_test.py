#!/usr/bin/python3

""" Max integer - Unittest"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        # Test that the function returns the maximum integer in a list
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_max_integer_empty_list(self):
        # Test that the function returns None when passed an empty list
        self.assertIsNone(max_integer([]))

    def test_max_integer_invalid_input(self):
        # Test that the function raises a TypeError when passed invalid input
        with self.assertRaises(TypeError):
            max_integer("not a list")
        with self.assertRaises(TypeError):
            max_integer([1, 2, "not an int"])

if __name__ == '__main__':
    unittest.main()
