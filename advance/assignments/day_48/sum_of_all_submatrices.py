"""
Problem Description
Given a 2D Matrix A of dimensions N*N, we need to return the sum of all possible submatrices.



Problem Constraints
1 <= N <=30

0 <= A[i][j] <= 10



Input Format
Single argument representing a 2-D array A of size N x N.



Output Format
Return an integer denoting the sum of all possible submatrices in the given matrix.



Example Input
A = [ [1, 1]
      [1, 1] ]


Example Output
16


Example Explanation
Number of submatrices with 1 elements = 4, so sum of all such submatrices = 4 * 1 = 4
Number of submatrices with 2 elements = 4, so sum of all such submatrices = 4 * 2 = 8
Number of submatrices with 3 elements = 0
Number of submatrices with 4 elements = 1, so sum of such submatrix = 4
Total Sum = 4+8+4 = 16
"""

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def getElementContribution(self,i,j,n,m):
        return (i+1)*(j+1)*(n-i)*(m-j)

    def solve(self,A):
        n = len(A)
        m = len(A[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                ans += self.getElementContribution(i,j,n,m) * A[i][j]
        return ans

solu = Solution()
array = [
    [
     [
        [1, 1],
        [1, 1]
     ]
    ], # 16
    ]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)