import os
import sys
sys.path.append(os.path.abspath('./linear_search/'))

import unittest
from linear_search import linear_search

arr = [1, 6, 8, 3, 4, 6, 9, 0, 2]

class LinearSearchTest(unittest.TestCase):
    def test_find_success(self):
        key = 6
        self.assertNotEqual(-1, linear_search(arr, key))

    def test_not_found(self):
        key = 7777
        self.assertEqual(-1, linear_search(arr, key))


if __name__ == "__main__":
    unittest.main()
