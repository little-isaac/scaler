"""
Problem Description
Given an array A of N non-negative numbers and a non-negative number B,
you need to find the number of subarrays in A with a sum less than B.
We may assume that there is no overflow.



Problem Constraints
1 <= N <= 103

1 <= A[i] <= 1000

1 <= B <= 107



Input Format
First argument is an integer array A.

Second argument is an integer B.



Output Format
Return an integer denoting the number of subarrays in A having sum less than B.



Example Input
Input 1:

 A = [2, 5, 6]
 B = 10
Input 2:

 A = [1, 11, 2, 3, 15]
 B = 10


Example Output
Output 1:

 4
Output 2:

 4


Example Explanation
Explanation 1:

 The subarrays with sum less than B are {2}, {5}, {6} and {2, 5},
Explanation 2:

 The subarrays with sum less than B are {1}, {2}, {3} and {2, 3}
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        ans = 0
        for i in range(n):
            sum = 0
            for j in range(i,n):
                sum = sum + A[j]
                if sum < B:
                    ans = ans + 1
        return ans



solu = Solution()
array = [
    [[2, 5, 6],10] , # 4
    [[1, 11, 2, 3, 15],10],  # 4
]
for A in array:
    ans = solu.solve(A[0],A[1])
    print("output for ",A," is ",ans)