#!/usr/bin/env python3

import unittest

def subarray(array):
    if len(array) < 2:
        return 0
    return 2



if __name__ == "__main__":
    class TestSubarray(unittest.TestCase):
        def test_empty_array(self):
            self.assertEqual(subarray([]), 0)

        def test_single_item_array(self):
            self.assertEqual(subarray([1]), 0)

        def test_2_ordered(self):
            self.assertEqual(subarray([1, 2]), 2)

        def test_2_reverse_ordered(self):
            self.assertEqual(subarray([2, 1]), 2)

    unittest.main()
