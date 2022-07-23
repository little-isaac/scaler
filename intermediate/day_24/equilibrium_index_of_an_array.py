"""
Problem Description
You are given an array A of integers of size N.

Your task is to find the equilibrium index of the given array

The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.

NOTE:

Array indexing starts from 0.
If there is no equilibrium index then return -1.
If there are more than one equilibrium indexes then return the minimum index.



Problem Constraints
1 <= N <= 105
-105 <= A[i] <= 105


Input Format
First arugment is an array A .


Output Format
Return the equilibrium index of the given array. If no such index is found then return -1.


Example Input
Input 1:
A=[-7, 1, 5, 2, -4, 3, 0]
Input 2:

A=[1,2,3]


Example Output
Output 1:
3
Output 2:

-1


Example Explanation
Explanation 1:
3 is an equilibrium index, because: 
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]
Explanation 1:

There is no such index.
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def rangeSum(self, l, r, pf):
        if l == 0:
            return pf[r]
        else:
            return pf[r] - pf[l-1]

    def prefixSum(self,A):
        n = len(A)
        pf = [0] * n
        pf[0] = A[0]
        for i in range(1,n):
            pf[i] = pf[i-1] + A[i]
        return pf
    def solve(self, A):
        n = len(A)
        prefixSum = self.prefixSum(A)
        for i in range(len(A)):
            if i == 0:
                leftSum = 0
            else:
                leftSum = self.rangeSum(0,i-1,prefixSum)
            rightSum = self.rangeSum(i+1,n-1,prefixSum)
            if leftSum == rightSum:
                return i
        return -1



solu = Solution()
array = [
    [-7, 1, 5, 2, -4, 3, 0], # 3
    [1,2,3]  # -1
]
for A in array:
    ans = solu.solve(A)
    print("output for ",A," is ",ans)