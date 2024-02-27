import os
import sys
sys.path.append(os.path.abspath('.'))

import unittest
from binary_search import binary_search

arr = [1, 6, 8, 3, 4, 6, 9, 0, 2]
arr.sort()

class BinarySearchTest(unittest.TestCase):
    def test_find_success(self):
        key = 6
        l = 0
        r = len(arr) - 1
        self.assertNotEqual(-1, binary_search(arr, key, l, r))

    def test_not_found(self):
        key = 7777
        l = 0
        r = len(arr) - 1
        self.assertEqual(-1, binary_search(arr, key, l, r))


if __name__ == "__main__":
    unittest.main()
