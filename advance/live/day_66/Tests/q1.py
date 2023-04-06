import unittest
import os
import sys
sys.path.append(os.getcwd())
import time

from advance.live.day_66.q1 import Solution


class Q1Tests(unittest.TestCase):

    inputOutput = [[2,3,4,5,8],[3,6,10,15,36]]

    def test_normal_array(self):

        objSol = Solution()
        for i in range(len(self.inputOutput[0])):
            input = self.inputOutput[0][i]
            output = self.inputOutput[1][i]
            ans = objSol.solve(input)
            self.assertEqual(ans, output)

if __name__ == '__main__':
    unittest.main()