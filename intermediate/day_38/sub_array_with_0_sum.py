"""
Problem Description
Given an array A of N integers.

Find the largest continuous sequence in a array which sums to zero.



Problem Constraints
1 <= N <= 106

-107 <= A[i] <= 107



Input Format
Single argument which is an integer array A.



Output Format
Return an array denoting the longest continuous sequence with total sum of zero.

NOTE : If there are multiple correct answers, return the sequence which occurs first in the array.



Example Input
A = [1,2,-2,4,-4]


Example Output
[2,-2,4,-4]


Example Explanation
[2,-2,4,-4] is the longest sequence with total sum of zero.
"""

class Solution:
	# @param A : list of integers
	# @return a list of integers
    def pSum(self,A):
        n = len(A)
        pf = [0] * n
        pf[0] = A[0]
        for i in range(1,n):
            pf[i] = pf[i-1] + A[i]
        return pf

    def solve(self, A):
        n = len(A)
        pf = set(self.pSum(A))
        if len(pf) < n or 0 in pf:
            return 1
        return 0

solu = Solution()
array = [
    [[1, 2, 3, 4, 5]] , # [2,-2,4,-4]
    [[-1, 1]] , # [2,-2,4,-4]
    [[ 96, -71, 18, 66, -39, -32, -16, -83, -11, -92, 55, 66, 93, 5, 50, -45, 66, -28, 69, -4, -34, -87, -32, 7, -53, 33, -12, -94, -80, -71, 48, -93, 62 ]] , # [2,-2,4,-4]
]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)