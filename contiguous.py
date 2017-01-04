#!/usr/bin/env python3

import unittest

def subarray(array):
    contiguous_subarray_length = 0
    if array != []:
        return contiguous_subarray_length + 1
    return contiguous_subarray_length

if __name__ == "__main__":
    class TestSubarray(unittest.TestCase):
        def test_empty_array(self):
            self.assertEqual(subarray([]), 0)

        def test_single_item_array(self):
            self.assertEqual(subarray([1]), 1)

    unittest.main()
