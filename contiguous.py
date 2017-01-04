#!/usr/bin/env python3

import unittest

def subarray(array):
    return 0

if __name__ == "__main__":
    class TestSubarray(unittest.TestCase):
        def test_empty_array(self):
            self.assertEqual(subarray([]), 0)

        def test_single_item_array(self):
            self.assertEqual(subarray([1]), 0)

        def test_2_ordered(self):
            self.assertEqual(subarray([1, 2]), 2)

    unittest.main()
