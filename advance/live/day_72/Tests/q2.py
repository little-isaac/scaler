import unittest
import os
import sys
sys.path.append(os.getcwd())
import time

from advance.live.day_72.q2 import Solution

class Q1Tests(unittest.TestCase):

    inputOutput = [[5,9],"95"]
    inputOutput1 = [[5,3,9],"953"]
    inputOutput2 = [[15,34,9],"93415"]
    inputOutput3 = [[33,4,51,9],"951433"]
    inputOutput4 = [[3,30,34,5,9],"9534330"]

    def test_normal_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput[0])

        self.assertEqual(ans, self.inputOutput[1])
    def test_1_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput1[0])

        self.assertEqual(ans, self.inputOutput1[1])
    def test_2_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput2[0])

        self.assertEqual(ans, self.inputOutput2[1])
    def test_3_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput3[0])

        self.assertEqual(ans, self.inputOutput3[1])

    def test_4_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput4[0])

        self.assertEqual(ans, self.inputOutput4[1])

if __name__ == '__main__':
    unittest.main()