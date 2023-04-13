import unittest
import os
import sys
sys.path.append(os.getcwd())
import time

from advance.live.day_69.q4 import Solution

class Q1Tests(unittest.TestCase):

    inputOutput = [[[7,10,11,14],[3,8,9]],[3,7,8,9,10,11,14]]
    inputOutput1 = [[[3,6,10],[5,9]],[3,5,6,9,10]]

    def test_normal_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput[0][0],self.inputOutput[0][1])

        self.assertEqual(ans, self.inputOutput[1])

    def test_normal_array1(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput1[0][0],self.inputOutput1[0][1])

        self.assertEqual(ans, self.inputOutput1[1])

if __name__ == '__main__':
    unittest.main()