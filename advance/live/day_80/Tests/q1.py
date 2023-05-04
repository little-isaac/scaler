import unittest
import os
import sys
sys.path.append(os.getcwd())
import time

from advance.live.day_80.q1 import Solution

class Q1Tests(unittest.TestCase):

    inputOutput = ["abcdcba",3]
    inputOutput1 = ["a",0]

    def test_normal_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput[0])

        self.assertEqual(ans, self.inputOutput[1])

    def test_normal1_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput1[0])

        self.assertEqual(ans, self.inputOutput1[1])

if __name__ == '__main__':
    unittest.main()