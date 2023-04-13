import unittest
import os
import sys
sys.path.append(os.getcwd())
import time

from advance.live.day_69.q1 import Solution

class Q1Tests(unittest.TestCase):

    inputOutput = [[2,6,10,14,20,4],[2,4,6,10,14,20]]

    def test_normal_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput[0])

        self.assertEqual(ans, self.inputOutput[1])

if __name__ == '__main__':
    unittest.main()