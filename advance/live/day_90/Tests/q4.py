import unittest
import os
import sys
sys.path.append(os.getcwd())
import time

from advance.live.day_90.q4 import Solution

class Q1Tests(unittest.TestCase):

    inputOutput = [5,21]

    def test_normal_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput[0])

        self.assertEqual(ans, self.inputOutput[1])

if __name__ == '__main__':
    unittest.main()