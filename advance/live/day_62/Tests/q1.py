import unittest
import os
import sys
sys.path.append(os.getcwd())
import time

from advance.live.day_62.q1 import Solution

class Q1Tests(unittest.TestCase):
    normalArray = [[3,3,4,-5,-2,2,1,-3,3,-1,5,-4,-1], 10]
    zeroPrefixSum = [[4,-3,-1,2,-2], 5]
    def test_normal_array(self):
        time.sleep(3)
        objSol = Solution()
        ans = objSol.solve(self.normalArray[0])
        self.assertEqual(ans, self.normalArray[1])
    def test_zero_prefix_sum_array(self):
        time.sleep(3)
        objSol = Solution()
        ans = objSol.solve(self.zeroPrefixSum[0])
        self.assertEqual(ans, self.zeroPrefixSum[1])

if __name__ == '__main__':
    unittest.main()