"""
Problem Description
Given a row-wise and column-wise sorted matrix A of size N * M.
Return the maximum non-empty submatrix sum of this matrix.


Problem Constraints
1 <= N, M <= 1000
-109 <= A[i][j] <= 109


Input Format
The first argument is a 2D integer array A.


Output Format
Return a single integer that is the maximum non-empty submatrix sum of this matrix.


Example Input
Input 1:-
    -5 -4 -3
A = -1  2  3
     2  2  4
Input 2:-
    1 2 3
A = 4 5 6
    7 8 9


Example Output
Output 1:-
12
Output 2:-
45


Example Explanation
Expanation 1:-
The submatrix with max sum is 
-1 2 3
 2 2 4
 Sum is 12.
Explanation 2:-
The largest submatrix with max sum is 
1 2 3
4 5 6
7 8 9
The sum is 45.
"""

class Solution:
    # @param A : list of list of integers
     # @return an long
    def getPrefixSumMatrix(self,A):
        n = len(A)
        m = len(A[0])
        pfSum = [[0] * m for _ in range(n)]
        for i in range(n):
            pfSum[i][0] =  A[i][0]
            for j in range(1,m):
                pfSum[i][j] = pfSum[i][j-1] + A[i][j]
        # return pfSum
        for j in range(m):
            pfSum[0][j] =  pfSum[0][j]
            for i in range(1,n):
                pfSum[i][j] = pfSum[i-1][j] + pfSum[i][j]
        return pfSum

    def getSumOfSubMatrix(self,pfSum,tl,br):
            x1 = tl[0] -1
            y1 = tl[1] -1
            x2 = br[0] -1
            y2 = br[1] -1
            sum = pfSum[x2][y2]
            if y1 > 0:
                sum = sum - pfSum[x2][y1-1]
            if x1 > 0:
                sum = sum - pfSum[x1-1][y2]
            if x1 > 0 and y1 > 0:
                sum = sum + pfSum[x1-1][y1-1]
            return sum
    def solve(self, A):
        n = len(A)
        m = len(A[0])
        i = 0
        j = m-1
        pfSum = self.getPrefixSumMatrix(A)
        ans = float("-inf")
        for i in range(n):
            for j in range(m):
                sum1 = self.getSumOfSubMatrix(pfSum,[i+1,j+1],[i+1,m])
                sum2 = self.getSumOfSubMatrix(pfSum,[i+1,j+1],[n,j+1])
                sum3 = self.getSumOfSubMatrix(pfSum,[i+1,j+1],[n,m])
                ans = max(ans,sum1,sum2,sum3)
        return ans


solu = Solution()
array = [
    [
        [ [-5, -4, -3],
          [-1, 2, 3],
          [2, 2, 4] ],

    ], #
    [
        [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
    ],
    [
        [
            [-83, -73, -70, -61],
            [-56, -48, -13, 4],
            [38, 48, 71, 71]
        ]
    ],
    [
        [
            [-29, 57],
            [-28, 60],
            [-11, 70],
            [15, 99]
        ]
    ]
    ]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)