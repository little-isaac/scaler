import unittest
import os
import sys
sys.path.append(os.getcwd())
import time

from advance.live.day_69.q6 import Solution

class Q1Tests(unittest.TestCase):

    inputOutput = [[10,3,7,5,8,4,2,1,3],[1,2,3,4,5,6,7,8,10]]

    def test_normal_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput[0])

        self.assertEqual(ans, self.inputOutput[1])

if __name__ == '__main__':
    unittest.main()