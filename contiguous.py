#!/usr/bin/env python3

import unittest

def subarray(array):
    if len(array) == 0:
        return 0
    else:
        return max(longest_continugous(array), subarray(array[1:]))

def longest_continugous(array):
    array_length = len(array)

    if max(array) - min(array) == array_length - 1:
        return array_length
    else:
        return longest_continugous(array[:-1])

if __name__ == "__main__":
    class TestSubarray(unittest.TestCase):
        def test_empty_array(self):
            self.assertEqual(subarray([]), 0)

        def test_single_item_array(self):
            self.assertEqual(subarray([1]), 1)

        def test_2_ordered(self):
            self.assertEqual(subarray([1, 2]), 2)

        def test_2_reverse_ordered(self):
            self.assertEqual(subarray([2, 1]), 2)

        def test_1_discontiguous(self):
            self.assertEqual(subarray([1, 3]), 1)

        def test_1_discontiguous_reverse_order(self):
            self.assertEqual(subarray([3, 1]), 1)

        def test_3_ordered(self):
            self.assertEqual(subarray([1, 2, 3]), 3)

        def test_3_jumbled(self):
            self.assertEqual(subarray([3, 1, 2]), 3)

        def test_3_another_jumbled(self):
            self.assertEqual(subarray([2, 1, 3]), 3)

        def test_3_with_discontiguous(self):
            self.assertEqual(subarray([2, 1, 3, 5]), 3)

        def test_3_with_discontiguous_reversed(self):
            self.assertEqual(subarray([5, 1, 3, 2]), 3)

        def test_3_with_larger_discontiguous(self):
            self.assertEqual(subarray([2, 1, 3, 5, 6]), 3)

        def test_4_with_larger_discontiguous_in_front_of_list(self):
            self.assertEqual(subarray([2, 1, 3, 5, 6, 7, 8]), 4)

    unittest.main()
