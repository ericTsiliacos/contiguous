#!/usr/bin/env python3

import unittest
import sys

def subarray(array):
    array_length = len(array)

    if array_length == 0:
        return 0

    if max(array) - min(array) == array_length - 1:
        return array_length

    return max(subarray(array[:-1]), subarray(array[1:]))

if __name__ == "__main__":
    class TestSubarray(unittest.TestCase):
        def test_empty_array(self):
            self.assertEqual(subarray([]), 0)

        def test_single_item_array(self):
            self.assertEqual(subarray([1]), 1)

        def test_2_contiguous(self):
            self.assertEqual(subarray([1, 2]), 2)

        def test_2_discontiguous(self):
            self.assertEqual(subarray([1, 3]), 1)

        def test_3_discontiguous(self):
            self.assertEqual(subarray([4, 1, 2]), 2)

    unittest.main()
