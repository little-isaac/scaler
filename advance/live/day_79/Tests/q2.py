import unittest
import os
import sys
sys.path.append(os.getcwd())
import time

from advance.live.day_79.q2 import Solution

class Q1Tests(unittest.TestCase):

    inputOutput = [[[-3,0,1,3,6,8,11,14,18,25],5],True]
    inputOutput1 = [[[1,4,6],2],True]
    inputOutput2 = [[[1,4,6],4],False]

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