import unittest
import os
import sys
sys.path.append(os.getcwd())
import time

from advance.live.day_90.q2 import Solution

class Q1Tests(unittest.TestCase):

    inputOutput = [[[3,10,2,12,19,6,8,10,14],4],[12,2,10,3,19,6,8,10,14]]

    def test_normal_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput[0][0],self.inputOutput[0][1])

        self.assertEqual(ans, self.inputOutput[1])

if __name__ == '__main__':
    unittest.main()