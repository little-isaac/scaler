import unittest
import os
import sys
sys.path.append(os.getcwd())
import time

from advance.live.day_79.q3 import Solution

class Q1Tests(unittest.TestCase):

    inputOutput = [[[3,5,4,7,3,6,5,4,1,2]],25]
    inputOutput1 = [[[1,2,3]],1]
    inputOutput2 = [[[4,5,6]],2]

    def test_normal_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput[0][0])

        self.assertEqual(ans, self.inputOutput[1])

    # def test_normal1_array(self):

    #     objSol = Solution()

    #     ans = objSol.solve(self.inputOutput1[0][0])

    #     self.assertEqual(ans, self.inputOutput1[1])

    # def test_normal2_array(self):

    #     objSol = Solution()

    #     ans = objSol.solve(self.inputOutput2[0][0])

    #     self.assertEqual(ans, self.inputOutput2[1])

if __name__ == '__main__':
    unittest.main()