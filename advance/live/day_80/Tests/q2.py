import unittest
import os
import sys
sys.path.append(os.getcwd())
import time

from advance.live.day_80.q2 import Solution

class Q1Tests(unittest.TestCase):

    inputOutput = ["abcdabc",[0, 0, 0, 0, 1, 2, 3]]
    inputOutput1 = ["a",[0]]
    inputOutput2 = ["aabaaba",[0, 1, 0, 1, 2, 3, 4]]

    def test_normal_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput[0])

        self.assertEqual(ans, self.inputOutput[1])

    def test_normal1_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput1[0])

        self.assertEqual(ans, self.inputOutput1[1])

    def test_normal2_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput2[0])

        self.assertEqual(ans, self.inputOutput2[1])

if __name__ == '__main__':
    unittest.main()