#!/usr/bin/env python3

import unittest

def subarray(array):
    return 0


if __name__ == "__main__":
    class TestSubarray(unittest.TestCase):
        def test_empty_array(self):
            self.assertEqual(subarray([]), 0)

    unittest.main()
