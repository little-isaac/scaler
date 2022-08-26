"""
Problem Description
On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row number A and index B, return the Bth indexed symbol in row A. (The values of B are 1-indexed.).



Problem Constraints
1 <= A <= 20

1 <= B <= 2A - 1



Input Format
First argument is an integer A.

Second argument is an integer B.



Output Format
Return an integer denoting the Bth indexed symbol in row A.



Example Input
Input 1:

 A = 2
 B = 1
Input 2:

 A = 2
 B = 2


Example Output
Output 1:

 0
Output 2:

 1


Example Explanation
Explanation 1:

 Row 1: 0
 Row 2: 01
Explanation 2:

 Row 1: 0
 Row 2: 01

"""

import sys
sys.setrecursionlimit(10**6)

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if B == 1:
            return 0
        if B % 2 == 0:
            parentData = self.solve(A-1,B//2)
            return 1-parentData
        else:
            parentData = self.solve(A-1,(B+1)//2)
            return parentData


solu = Solution()
array = [
    [2,1] , # 0
    [2,2] , # 1
    [9,175] , # 1
]
for A in array:
    ans = solu.solve(A[0],A[1])
    print("output for ",A," is ",ans)