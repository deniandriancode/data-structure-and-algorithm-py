import os
import sys
sys.path.append(os.path.abspath('./ternary_search/'))

import unittest
from ternary_search import ternary_search

arr = [1, 6, 8, 3, 4, 6, 9, 0, 2]
arr.sort()

class TernarySearchTest(unittest.TestCase):
    def test_find_success(self):
        key = 6
        l = 0
        r = len(arr) - 1
        self.assertNotEqual(-1, ternary_search(arr, key, l, r))

    def test_not_found(self):
        key = 7777
        l = 0
        r = len(arr) - 1
        self.assertEqual(-1, ternary_search(arr, key, l, r))


if __name__ == "__main__":
    unittest.main()
