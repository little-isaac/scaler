"""
Problem Description
Given a matrix of integers A of size N x M and multiple queries Q, for each query, find and return the submatrix sum.

Inputs to queries are top left (b, c) and bottom right (d, e) indexes of submatrix whose sum is to find out.

NOTE:

Rows are numbered from top to bottom, and columns are numbered from left to right.
Sum may be large, so return the answer mod 109 + 7.


Problem Constraints
1 <= N, M <= 1000
-100000 <= A[i] <= 100000
1 <= Q <= 100000
1 <= B[i] <= D[i] <= N
1 <= C[i] <= E[i] <= M



Input Format
The first argument given is the integer matrix A.
The second argument given is the integer array B.
The third argument given is the integer array C.
The fourth argument given is the integer array D.
The fifth argument given is the integer array E.
(B[i], C[i]) represents the top left corner of the i'th query.
(D[i], E[i]) represents the bottom right corner of the i'th query.



Output Format
Return an integer array containing the submatrix sum for each query.



Example Input
Input 1:

 A = [   [1, 2, 3]
         [4, 5, 6]
         [7, 8, 9]   ]
 B = [1, 2]
 C = [1, 2]
 D = [2, 3]
 E = [2, 3]
Input 2:

 A = [   [5, 17, 100, 11]
         [0, 0,  2,   8]    ]
 B = [1, 1]
 C = [1, 4]
 D = [2, 2]
 E = [2, 4]


Example Output
Output 1:

 [12, 28]
Output 2:

 [22, 19]


Example Explanation
Explanation 1:

 For query 1: Submatrix contains elements: 1, 2, 4 and 5. So, their sum is 12.
 For query 2: Submatrix contains elements: 5, 6, 8 and 9. So, their sum is 28.
Explanation 2:

 For query 1: Submatrix contains elements: 5, 17, 0 and 0. So, their sum is 22.
 For query 2: Submatrix contains elements: 11 and 8. So, their sum is 19.
 
"""

class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
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

    def solve(self, A, B, C, D, E):
        pfSum = self.getPrefixSumMatrix(A)
        n = len(B)
        ans = []
        for i in range(n):
            tl = [B[i],C[i]]
            br = [D[i],E[i]]
            ans.append(self.getSumOfSubMatrix(pfSum,tl,br))
        return ans



solu = Solution()
array = [
    [
     [   [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]
     ],
     [1, 2],[1, 2],[2, 3],[2, 3]
    ],
    [
        [   [5, 17, 100, 11],
         [0, 0,  2,   8]    ],
         [1,1],[1,4],[2,2],[2,4]
    ]
    ]
for A in array:
    ans = solu.solve(A[0],A[1],A[2],A[3],A[4])
    print("output for ",A," is ",ans)