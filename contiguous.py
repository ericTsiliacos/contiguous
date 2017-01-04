#!/usr/bin/env python3

import unittest

def subarray(array):
    contiguous_subarray_length = 0
    while array[contiguous_subarray_length:] != []:
        contiguous_subarray_length += 1
    return contiguous_subarray_length

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

    unittest.main()
