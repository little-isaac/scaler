import unittest
import os
import sys
sys.path.append(os.getcwd())
import time

from advance.live.day_72.q1 import Solution

class Q1Tests(unittest.TestCase):

    inputOutput1 = [[8,3,4],2]
    inputOutput2 = [[10,3,8,15,6,12,2,18,7,1],26]

    def test_1_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput1[0])

        self.assertEqual(ans, self.inputOutput1[1])

    def test_2_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput2[0])

        self.assertEqual(ans, self.inputOutput2[1])

if __name__ == '__main__':
    unittest.main()