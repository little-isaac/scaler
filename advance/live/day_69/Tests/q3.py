import unittest
import os
import sys
sys.path.append(os.getcwd())
import time

from advance.live.day_69.q3 import Solution

class Q1Tests(unittest.TestCase):

    inputOutput = [[2,8,4,7,6,-1],[-1,2,4,6,7,8]]

    def test_normal_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput[0])

        self.assertEqual(ans, self.inputOutput[1])

if __name__ == '__main__':
    unittest.main()