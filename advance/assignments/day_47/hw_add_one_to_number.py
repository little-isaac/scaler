"""
Problem Description
Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer. For example: for this problem, the following are some good questions to ask :

Q: Can the input have 0's before the most significant digit. Or, in other words, is 0 1 2 3 a valid input?
A: For the purpose of this question, YES
Q: Can the output have 0's before the most significant digit? Or, in other words, is 0 1 2 4 a valid output?
A: For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.


Problem Constraints
1 <= size of the array <= 1000000



Input Format
First argument is an array of digits.



Output Format
Return the array of digits after adding one.



Example Input
Input 1:

[1, 2, 3]


Example Output
Output 1:

[1, 2, 4]


Example Explanation
Explanation 1:

Given vector is [1, 2, 3].
The returned vector should be [1, 2, 4] as 123 + 1 = 124.
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        n = len(A)
        ans = []
        c = 1
        for i in range(n-1,-1,-1):
            if A[i] != 0 or i == n-1:
                a = A[i] + c
                if a < 10:
                    ans.append(a)
                    c = 0
                    continue
                ans.append(a % 10)
                ans.append(a//10)
        return ans[::-1]

solu = Solution()
array = [
    [[1, 2, 3]], # [1, 2, 4]
    [[0]], # [1]
    [[0,0]], # [1]
    ]
for A in array:
    ans = solu.plusOne(A[0])
    print("output for ",A," is ",ans)