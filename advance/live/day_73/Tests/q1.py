import unittest
import os
import sys
sys.path.append(os.getcwd())
import time

from advance.live.day_73.q1 import Solution

class Q1Tests(unittest.TestCase):

    inputOutput = [[3,8,1,0,6,2,4],[0,1,2,3,4,6,8]]
    inputOutput1 = [[3,8,2,0,10,2,4],[0,2,2,3,4,8,10]]

    def test_normal_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput[0])

        self.assertEqual(ans, self.inputOutput[1])

    def test_1_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput1[0])

        self.assertEqual(ans, self.inputOutput1[1])


if __name__ == '__main__':
    unittest.main()