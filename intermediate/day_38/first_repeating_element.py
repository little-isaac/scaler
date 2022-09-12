"""
Problem Description
Given an integer array A of size N, find the first repeating element in it.

We need to find the element that occurs more than once and whose index of the first occurrence is the smallest.

If there is no repeating element, return -1.



Problem Constraints
1 <= N <= 105

1 <= A[i] <= 109



Input Format
The first and only argument is an integer array A of size N.



Output Format
Return an integer denoting the first repeating element.



Example Input
Input 1:

 A = [10, 5, 3, 4, 3, 5, 6]
Input 2:

 A = [6, 10, 5, 4, 9, 120]


Example Output
Output 1:

 5
Output 2:

 -1


Example Explanation
Explanation 1:

 5 is the first element that repeats
Explanation 2:

 There is no repeating element, output -1
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        ans = -1
        hashA = {}
        for i in range(n):
            if A[i] not in hashA:
                hashA[A[i]] = i
            else:
                if hashA[A[i]] < ans or ans == -1:
                    ans = hashA[A[i]]
        if ans == -1:
            return -1
        return A[ans]
        

solu = Solution()
array = [
    [[8, 15, 1, 10, 5, 19, 19, 3, 5, 6, 6, 2, 8, 2, 12, 16, 3, ]] , # 8
    [[10, 5, 3, 4, 3, 5, 6]] , # 5
    [[6, 10, 5, 4, 9, 120]] , # -1
]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)


