#!/usr/bin/env python3

import unittest
import sys

def subarray(array):
    contiguous_subarray_length = 0
    maxiumum = 0
    minimum = sys.maxsize
    while array[contiguous_subarray_length:] != []:
        current_element = array[contiguous_subarray_length]
        maxiumum = current_element if current_element > maxiumum else maxiumum
        minimum = current_element if current_element < minimum else minimum
        contiguous_subarray_length += 1
    if contiguous_subarray_length == 0:
        return 0
    if maxiumum - minimum == contiguous_subarray_length - 1:
        return contiguous_subarray_length

    largest_subarray_from_start = subarray(array[:-1])
    largest_subarray_from_end = subarray(array[1:])
    if largest_subarray_from_start > largest_subarray_from_end:
        return largest_subarray_from_start
    return largest_subarray_from_end

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
