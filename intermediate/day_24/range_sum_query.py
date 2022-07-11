"""
Problem Description
You are given an integer array A of length N.
You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
For each query, you have to find the sum of all elements from L to R indices in A (1 - indexed).
More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.



Problem Constraints
1 <= N, M <= 105
1 <= A[i] <= 109
1 <= L <= R <= N


Input Format
The first argument is the integer array A.
The second argument is the 2D integer array B.


Output Format
Return an integer array of length M where ith element is the answer for ith query in B.


Example Input
Input 1:
A = [1, 2, 3, 4, 5]
B = [[1, 4], [2, 3]]
Input 2:

A = [2, 2, 2]
B = [[1, 1], [2, 3]]


Example Output
Output 1:
[10, 5]
Output 2:

[2, 4]


Example Explanation
Explanation 1:
The sum of all elements of A[1 ... 4] = 1 + 2 + 3 + 4 = 10.
The sum of all elements of A[2 ... 3] = 2 + 3 = 5.
Explanation 2:

The sum of all elements of A[1 ... 1] = 2 = 2.
The sum of all elements of A[2 ... 3] = 2 + 2 = 4.
"""

class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
    def solve(self,A,B):
        return self.rangeSum(A,B)

    def rangeSum(self, A, B):
        n = len(A)
        bl = len(B)
        ans = [0] * bl
        pf = [0] * n
        pf[0] = A[0]
        for i in range(1,n):
            pf[i] = pf[i-1] + A[i]
        for j in range(0,len(B)):
            ele = B[j]
            l = ele[0] - 1
            r = ele[1] - 1
            if l == 0:
                ans[j] = pf[r]
            else:
                ans[j] = (pf[r] - pf[l-1])
        return ans

solu = Solution()
array = [
    [[1, 2, 3, 4, 5],[[1, 4], [1, 3]]], # 10 5
    [[2, 2, 2],[[1, 1], [2, 3]]]  # 2 4
]
for A in array:
    ans = solu.solve(A[0],A[1])
    print("output for ",A," is ",ans)