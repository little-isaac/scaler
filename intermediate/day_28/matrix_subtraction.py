"""
Problem Description

You are given two integer matrices A and B having same size(Both having same number of rows (N) and columns (M)). You have to subtract matrix A from B and return the resultant matrix. (i.e. return the matrix A - B).

If X and Y are two matrices of the same order (same dimensions). Then X - Y is a matrix of the same order as X and Y and its elements are obtained by subtracting the elements of Y from the corresponding elements of X. Thus if Z = [z[i][j]] = X - Y, then [z[i][j]] = [x[i][j]] – [y[i][j]].



Problem Constraints

1 <= N, M <= 103

-109 <= A[i][j], B[i][j] <= 109



Input Format

First argument is a 2D integer matrix A.

Second argument is a 2D integer matrix B.



Output Format

Return a 2D matrix denoting A - B.



Example Input

Input 1:

 A = [[1, 2, 3],            B = [[9, 8, 7],
      [4, 5, 6],                 [6, 5, 4],
      [7, 8, 9]]                 [3, 2, 1]]
Input 2:

 A = [[1, 1]]               B = [[2, 3]]


Example Output

Output 1:

 [[-8, -6, -4],
  [-2, 0, 2],
  [4, 6, 8]]
Output 2:

 [[-1, -2]]


Example Explanation

Explanation 1:

 image - https://s3.ap-south-1.amazonaws.com/scaler-production-domestic/public_assets/assets/000/000/015/original/11463.png?1614376240
Explanation 2:

 [[1, 1]] - [[2, 3]] = [[1 - 2, 1 - 3]] = [[-1, -2]]
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
                ans[i][j] = A[i][j] - B[i][j]
        return ans


solu = Solution()
array = [
    [[[1, 2, 3],[4, 5, 6],[7, 8, 9]],[[9, 8, 7],[6, 5, 4],[3, 2, 1]]] , # [[10, 10, 10], [10, 10, 10], [10, 10, 10]]
    [[[1,1]],[[2,3]]] # [[-1,-2]]
]
for A in array:
    ans = solu.solve(A[0],A[1])
    print("output for ",A," is ",ans)