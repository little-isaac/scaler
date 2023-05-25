import unittest
import os
import sys
sys.path.append(os.getcwd())
import time

from advance.live.day_91.q3 import Solution

class Q1Tests(unittest.TestCase):

    inputOutput = [[],[]]

    def test_normal_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput[0])

        self.assertEqual(ans, self.inputOutput[1])

if __name__ == '__main__':
    unittest.main()