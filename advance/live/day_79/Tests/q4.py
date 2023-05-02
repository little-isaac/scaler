import unittest
import os
import sys
sys.path.append(os.getcwd())
import time

from advance.live.day_79.q4 import Solution

class Q1Tests(unittest.TestCase):

    inputOutput = [[[-1, 2, 1, -4],1],2]
    inputOutput1 = [[[-2, -1, 2, 4, 5],10],11]
    inputOutput2 = [[[4,5,6],2],2]

    def test_normal_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput[0][0], self.inputOutput[0][1])

        self.assertEqual(ans, self.inputOutput[1])

    def test_normal1_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput1[0][0],self.inputOutput1[0][1])

        self.assertEqual(ans, self.inputOutput1[1])

    # def test_normal2_array(self):

    #     objSol = Solution()

    #     ans = objSol.solve(self.inputOutput2[0][0])

    #     self.assertEqual(ans, self.inputOutput2[1])

if __name__ == '__main__':
    unittest.main()