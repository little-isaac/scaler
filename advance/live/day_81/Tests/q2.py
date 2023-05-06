import unittest
import os
import sys
sys.path.append(os.getcwd())
import time

from advance.live.day_81.q2 import Solution

import unittest

class Q1Tests(unittest.TestCase):

    def test_solve(self):
        s = Solution()
        self.assertEqual(s.solve("ab", "abab"), 3)
        self.assertEqual(s.solve("daba", "aabdabad"), 4)
        self.assertEqual(s.solve("aaa", "aaaaa"), 3)
        self.assertEqual(s.solve("abc", "cbaebabacd"), 2)

if __name__ == '__main__':
    unittest.main()