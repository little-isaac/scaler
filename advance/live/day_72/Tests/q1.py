import unittest
import os
import sys
sys.path.append(os.getcwd())
import time

from advance.live.day_72.q1 import Solution

class Q1Tests(unittest.TestCase):

    inputOutput1 = [[8,3,4],2]
    inputOutput2 = [[10,3,8,15,6,12,2,18,7,1],26]
    inputOutput3 = [[6, 12, 10, 17, 10, 22, 9, 19, 21, 31, 26, 8 ],21]

    def test_3_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput3[0])

        self.assertEqual(ans, self.inputOutput3[1])

if __name__ == '__main__':
    unittest.main()