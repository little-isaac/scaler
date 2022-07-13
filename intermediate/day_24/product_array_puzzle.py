"""
Given an array of integers A, find and return the product array of the same size where the ith element of the product array will be equal to the product of all the elements divided by the ith element of the array.

Note: It is always possible to form the product array with integer (32 bit) values. Solve it without using the division operator.


Input Format

The only argument given is the integer array A.
Output Format

Return the product array.
Constraints

1 &lt;= length of the array &lt;= 1000
1 &lt;= A[i] &lt;= 10
For Example

Input 1:
    A = [1, 2, 3, 4, 5]
Output 1:
    [120, 60, 40, 30, 24]

Input 2:
    A = [5, 1, 10, 1]
Output 2:
    [10, 50, 5, 50]

"""
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        left = [0] * n
        right = [0] * n
        left[0] = 1
        right[n-1] = 1
        ans = [0] * n
        for i in range(1,n):
            # multiply ith element from left to right
            # we are using i - 1 because we want prev element to multiply
            left[i] = left[i-1] * A[i-1]
        for j in range(n-2,-1,-1):
            # multiply jth element from right to left
            # we are using j + 1 because we want next element to multiply
            right[j] = right[j+1] * A[j+1]
        for k in range(0,n):
            ans[k] = left[k] * right[k]

        return ans

solu = Solution()
array = [
    [1,2,3,4,5], # [120, 60, 40, 30, 24]
    [5, 1, 10, 1], # [10, 50, 5, 50]
]
for A in array:
    ans = solu.solve(A)
    print("output for ",A," is ",ans)