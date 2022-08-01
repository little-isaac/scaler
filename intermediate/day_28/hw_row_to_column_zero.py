"""
Problem Description
You are given a 2D integer matrix A, make all the elements in a row or column zero if the A[i][j] = 0. Specifically, make entire ith row and jth column zero.



Problem Constraints
1 <= A.size() <= 103

1 <= A[i].size() <= 103

0 <= A[i][j] <= 103



Input Format
First argument is a vector of vector of integers.(2D matrix).



Output Format
Return a vector of vector after doing required operations.



Example Input
Input 1:

[1,2,3,4]
[5,6,7,0]
[9,2,0,4]


Example Output
Output 1:

[1,2,0,0]
[0,0,0,0]
[0,0,0,0]


Example Explanation
Explanation 1:

A[2][4] = A[3][3] = 0, so make 2nd row, 3rd row, 3rd column and 4th column zero.
"""

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        n = len(A)
        m = len(A[0])
        cZero = [-1]*m
        rZero = [-1]*n
        for i in range(n):
            for j in range(m):
                if A[i][j] == 0:
                    cZero[j] = 1
                    rZero[i] = 1
        for i in range(n):
            isRowZero = rZero[i] == 1
            for j in range(m):
                isColZero = cZero[j] == 1
                if isRowZero or isColZero:
                    A[i][j] = 0
        return A


solu = Solution()
array = [
    [[[1,2,3,4],[5,6,7,0],[9,2,0,4]]] , # [[1,2,0,0],[0,0,0,0],[0,0,0,0]]
]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)