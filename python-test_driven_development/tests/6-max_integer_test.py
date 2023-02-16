#!/usr/bin/python3

""" Max integer - Unittest"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_at_end(self):
        # Test that the function returns the maximum integer when it is at the end of the list
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_max_at_beginning(self):
        # Test that the function returns the maximum integer when it is at the beginning of the list
        self.assertEqual(max_integer([3, 2, 1]), 3)

    def test_max_in_middle(self):
        # Test that the function returns the maximum integer when it is in the middle of the list
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_one_negative_number(self):
        # Test that the function returns the maximum integer when there is one negative number in the list
        self.assertEqual(max_integer([1, 2, -3]), 2)

    def test_only_negative_numbers(self):
        # Test function returns the maximum integer when all numbers in the list are negative
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_list_of_one_element(self):
        # Test function returns the single element in the list when there is only one element
        self.assertEqual(max_integer([42]), 42)

    def test_empty_list(self):
        # Test function returns None when passed an empty list
        self.assertIsNone(max_integer([]))

    def test_invalid_input(self):
        # Test that the function raises a TypeError when passed invalid input
        with self.assertRaises(TypeError):
            max_integer("not a list")
        with self.assertRaises(TypeError):
            max_integer([1, 2, "not an int"])

if __name__ == '__main__':
    unittest.main()
