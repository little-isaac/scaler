import unittest
import os
import sys
sys.path.append(os.getcwd())
import time

from advance.live.day_69.q5 import Solution

class Q1Tests(unittest.TestCase):
                                         
    inputOutput = [[[4,8,-1,2,6,9,11,3,4,7,13,20],2,6,9],[4,8,-1,2,3,4,6,7,9,11,13,20]]

    def test_normal_array(self):

        objSol = Solution()

        ans = objSol.solve(self.inputOutput[0][0],self.inputOutput[0][1],self.inputOutput[0][2],self.inputOutput[0][3])

        self.assertEqual(ans, self.inputOutput[1])

if __name__ == '__main__':
    unittest.main()