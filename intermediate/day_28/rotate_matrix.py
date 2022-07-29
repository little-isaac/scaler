"""
Problem Description
You are given a n x n 2D matrix A representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.

Note: If you end up using an additional array, you will only receive partial score.



Problem Constraints
1 <= n <= 1000



Input Format
First argument is a 2D matrix A of integers



Output Format
Return the 2D rotated matrix.



Example Input
Input 1:

 [
    [1, 2],
    [3, 4]
 ]
Input 2:

 [
    [1]
 ]


Example Output
Output 1:

 [
    [3, 1],
    [4, 2]
 ]
Output 2:

 [
    [1]
 ]


Example Explanation
Explanation 1:

 After rotating the matrix by 90 degree:
 1 goes to 2, 2 goes to 4
 4 goes to 3, 3 goes to 1
Explanation 2:

 2D array remains the ssame as there is only element.
"""

class Solution:
    # @param A : list of list of integers
    def transpose(self, A):
        n = len(A)
        m = len(A[0])
        for i in range(1,n):
            for j in range(0,i):
                A[j][i],A[i][j] = A[i][j],A[j][i]
        return A
    def replaceArray(self,arr,s,e):
        i = s
        j = e
        while(i<j):
            arr[i],arr[j] = arr[j],arr[i]
            i = i + 1
            j = j - 1
        return arr
    def solve(self, A):
        transpose = self.transpose(A)
        n = len(transpose)
        for i in range(n):
            transpose[i] = self.replaceArray(transpose[i],0,len(transpose[i])-1)
        return transpose



solu = Solution()
array = [
    [[[1, 2],[3, 4]]] , # [[3, 1],[4, 2]]
    [[[1]]], #[[1]]
]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)