"""
Problem Description
You are given an array A of N integers. Return the count of elements with frequncy 1 in the given array.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109


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
1
Output 2:
2


Example Explanation
For Input 1:
Only the element 4 has a frequency 1.
For Input 2:
The elements 9 and 1 has a frequncy 1.
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        hashSet = {}
        for i in range(n):
            ele = A[i]
            if ele in hashSet:
                hashSet[ele] = hashSet[ele] + 1
            else:
                hashSet[ele] = 1
        ans = 0
        for i in hashSet:
            if hashSet[i] == 1:
                ans = ans + 1
        return ans


solu = Solution()
array = [
    [3, 4, 3, 6, 6], # 3
    ]
for A in array:
    ans = solu.solve(A)
    print("output for ",A," is ",ans)