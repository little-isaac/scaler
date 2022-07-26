"""
Problem Description
You are given two integer matrices A(having M X N size) and B(having N X P). You have to multiply matrix A with B and return the resultant matrix. (i.e. return the matrix AB).

image - https://s3.ap-south-1.amazonaws.com/scaler-production-domestic/public_assets/assets/000/000/008/original/11464-1.png?1614375643



Problem Constraints
1 <= M, N, P <= 100

-100 <= A[i][j], B[i][j] <= 100



Input Format
First argument is a 2D integer matrix A.

Second argument is a 2D integer matrix B.



Output Format
Return a 2D integer matrix denoting AB.



Example Input
Input 1:

 A = [[1, 2],            B = [[5, 6],
      [3, 4]]                 [7, 8]] 
Input 2:

 A = [[1, 1]]            B = [[2],
                              [3]] 


Example Output
Output 1:

 [[19, 22],
  [43, 50]]
Output 2:

 [[5]]


Example Explanation
Explanation 1:

 image - https://s3.ap-south-1.amazonaws.com/scaler-production-domestic/public_assets/assets/000/000/009/original/11464-2.png?1614375673
Explanation 2:

 [[1, 1]].[[2, 3]] = [[1 * 2 + 1 * 3]] = [[5]]
"""
class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        m = len(A)
        n = len(A[0])
        p = len(B[0])
        ans = [[0] * p for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for x in range(p):
                    ans[i][x] += A[i][j]*B[j][x]
        return ans

solu = Solution()
array = [
    [[[1, 2],[3, 4]],[[5, 6],[7, 8]]] , # [[19, 22],[43, 50]]
    [[[1, 1]],[[2],[3]]] # [[5]]
]
for A in array:
    ans = solu.solve(A[0],A[1])
    print("output for ",A," is ",ans)