"""
Problem Description
You are given an array A of N integers. You will have to return number of distinct elements of the array.

Problem Constraints
1 <= N <= 10^5
1 <= A[i] <= 10^9


Input Format
First argument A is an array of integers.


Output Format
Return an integer.


Example Input
Input 1:
A = [3, 4, 3, 6, 6]
Input 2:
A = [3, 3, 3, 9, 0, 1, 0]


Example Output
Output 1:
3
Output 2:
4

Example Explanation
For Input 1:
The distinct elements of the array are 3, 4 and 6.
For Input 2:
The distinct elements of the array are 3, 9, 0 and 1.
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        hashSet = {}
        ans = 0
        for i in range(n):
            ele = A[i]
            if ele not in hashSet:
                ans = ans + 1
                hashSet[ele] = i

        return ans

solu = Solution()
array = [
    [3, 4, 3, 6, 6], # 3
    ]
for A in array:
    ans = solu.solve(A)
    print("output for ",A," is ",ans)