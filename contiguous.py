#!/usr/bin/env python3

import unittest
import sys

def subarray(array, length):
    max_length = 1
    for start_index, element in enumerate(array):
        minimum = maximum = array[start_index]
        end_index = start_index + 1
        while end_index < length:
            end_element = array[end_index]
            minimum = min(minimum, end_element)
            maximum = max(maximum, end_element)
            difference = maximum - minimum
            if difference == end_index - start_index:
                max_length = max(max_length, difference + 1)
            end_index += 1
    return max_length


if __name__ == "__main__":
    class TestSubarray(unittest.TestCase):
        def test_single_item_array(self):
            self.assertEqual(subarray([1], 1), 1)

        def test_2_contiguous(self):
            self.assertEqual(subarray([1, 2], 2), 2)

        def test_2_discontiguous(self):
            self.assertEqual(subarray([1, 3], 2), 1)

        def test_3_discontiguous(self):
            self.assertEqual(subarray([4, 1, 2], 3), 2)

        def test_sanity(self):
            self.assertEqual(subarray([10, 12, 11], 3), 3)
            self.assertEqual(subarray([14, 12, 11, 20], 4), 2)
            self.assertEqual(subarray([1, 56, 58, 57, 90, 92, 94, 93, 91, 45], 10), 5)

    unittest.main()
