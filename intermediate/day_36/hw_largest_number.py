"""
Problem Description
Given an array A of non-negative integers, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.



Problem Constraints
1 <= len(A) <= 100000
0 <= A[i] <= 2*109



Input Format
The first argument is an array of integers.



Output Format
Return a string representing the largest number.



Example Input
Input 1:

 A = [3, 30, 34, 5, 9]
Input 2:

 A = [2, 3, 9, 0]


Example Output
Output 1:

 "9534330"
Output 2:

 "9320"


Example Explanation
Explanation 1:

Reorder the numbers to [9, 5, 34, 3, 30] to form the largest number.
Explanation 2:

Reorder the numbers to [9, 3, 2, 0] to form the largest number 9320.
"""

from functools import cmp_to_key
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A = list(map(str,A))
        def compare(num1,num2):
            if num1 + num2 > num2 + num1:
                return -1
            else:
                return 1
        A = sorted(A,key=cmp_to_key(compare))
        if A[0] =='0':
            return 0
        return "".join(A)
    def largestNumberPrev(self, A):
        A = list(A)
        n = len(A)
        for i in range(n):
            A[i] = str(int(A[i]))
        for i in range(n):
            for j in range(i,n):
                if A[i]+A[j] < A[j]+A[i]:
                    A[i],A[j] = A[j],A[i]
        return ''.join(map(str, A))





solu = Solution()
array = [
    [[3, 30, 34, 5, 9]] , # "9534330"
    [[2, 3, 9, 0]] , # "9320"
]
for A in array:
    ans = solu.largestNumber(A[0])
    print("output for ",A," is ",ans)