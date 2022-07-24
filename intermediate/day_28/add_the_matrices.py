"""
Problem Description

You are given two matrices A & B of same size, you have to return another matrix which is the sum of A and B.



Problem Constraints

1 <= A.size(), B.size() <= 1000

1 <= A[i].size(), B[i].size() <= 1000

1 <= A[i][j], B[i][j] <= 1000



Input Format

First argument is vector of vector of integers representing matrix A.

Second argument is vecotor of vector of integers representing matrix B.



Output Format

You have to return a vector of vector of integers after doing required operations.



Example Input

Input 1:

A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
B = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]


Example Output

Output 1:

[[10, 10, 10], [10, 10, 10], [10, 10, 10]]


Example Explanation

Explanation 1:

A + B = [[1+9, 2+8, 3+7],[4+6, 5+5, 6+4],[7+3, 8+2, 9+1]] = [[10, 10, 10], [10, 10, 10], [10, 10, 10]].
"""
class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        n = len(A)
        m = len(A[0])
        ans = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j] = A[i][j] + B[i][j]
        return ans


solu = Solution()
array = [
    [[[1, 2, 3],[4, 5, 6],[7, 8, 9]],[[9, 8, 7],[6, 5, 4],[3, 2, 1]]] , # [[10, 10, 10], [10, 10, 10], [10, 10, 10]]
]
for A in array:
    ans = solu.solve(A[0],A[1])
    print("output for ",A," is ",ans)