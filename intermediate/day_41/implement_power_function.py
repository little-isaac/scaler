"""
Problem Description
Implement pow(A, B) % C.
In other words, given A, B and C, Find (AB % C).

Note: The remainders on division cannot be negative. In other words, make sure the answer you return is non-negative.



Problem Constraints
-109 <= A <= 109
0 <= B <= 109
1 <= C <= 109


Input Format
Given three integers A, B, C.


Output Format
Return an integer.


Example Input
A = 2, B = 3, C = 3


Example Output
2


Example Explanation
23 % 3 = 8 % 3 = 2
"""

import sys
sys.setrecursionlimit(10**6)

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    
    def solve(self, A, B, C):
         
        # Base Cases
        if (A == 0):
            return 0
        if (B == 0):
            return 1
         
        # If B is Even
        y = 0
        if (B % 2 == 0):
            y = self.solve(A, B / 2, C)
            y = (y * y) % C
         
        # If B is Odd
        else:
            y = A % C
            y = (y * self.solve(A, B - 1,
                                 C) % C) % C
        return ((y + C) % C)
    

    def pow(self, A, B, C):
        p = self.solve(A,B,C)
        return ((p % C) + C)%C


solu = Solution()
array = [
    [2,3,3] , # 1
    [-1,2,20] , # 1
    [-1,1,20] , # 1
]
for A in array:
    ans = solu.pow(A[0],A[1],A[2])
    print("output for ",A," is ",ans)