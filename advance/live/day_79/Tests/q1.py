import unittest
import os
import sys
sys.path.append(os.getcwd())
import time

from advance.live.day_79.q1 import Solution

class Q1Tests(unittest.TestCase):

    inputOutput = [[[3,7,8,12,19],15],True]
    inputOutput1 = [[[2,5,8,12,15],16],False]
    inputOutput2 = [[[-3,0,1,3,6,8,11,14,18,25],17],True]

    def test_normal_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput[0][0],self.inputOutput[0][1])

        self.assertEqual(ans, self.inputOutput[1])

    def test_normal1_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput1[0][0],self.inputOutput1[0][1])

        self.assertEqual(ans, self.inputOutput1[1])

    def test_normal2_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput2[0][0],self.inputOutput2[0][1])

        self.assertEqual(ans, self.inputOutput2[1])


if __name__ == '__main__':
    unittest.main()