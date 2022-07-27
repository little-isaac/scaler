"""
Problem Description
You are given a matrix A, you have to return another matrix which is the transpose of A.

NOTE: Transpose of a matrix A is defined as - AT[i][j] = A[j][i] ; Where 1 ≤ i ≤ col and 1 ≤ j ≤ row



Problem Constraints
1 <= A.size() <= 1000

1 <= A[i].size() <= 1000

1 <= A[i][j] <= 1000



Input Format
First argument is vector of vector of integers A representing matrix.



Output Format
You have to return a vector of vector of integers after doing required operations.



Example Input
Input 1:

A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
Input 2:

A = [[1, 2],[1, 2],[1, 2]]


Example Output
Output 1:

[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
Output 2:

[[1, 1, 1], [2, 2, 2]]


Example Explanation
Explanation 1:

clearly after converting rows to column and columns to rows of [[1, 2, 3],[4, 5, 6],[7, 8, 9]] we will get [[1, 4, 7], [2, 5, 8], [3, 6, 9]].
"""

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        n = len(A)
        m = len(A[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                ans[j][i] = A[i][j]
        return ans



solu = Solution()
array = [
    [[[1, 2, 3],[4, 5, 6],[7, 8, 9]]] , # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    [[[1, 2],[1, 2],[1, 2]]], #[[1, 1, 1], [2, 2, 2]]
]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)