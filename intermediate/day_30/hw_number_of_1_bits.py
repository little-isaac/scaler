"""
Problem Description
Write a function that takes an integer and returns the number of 1 bits it has.


Problem Constraints
1 <= A <= 109


Input Format
First and only argument contains integer A


Output Format
Return an integer as the answer


Example Input
Input1:
11


Example Output
Output1:
3


Example Explanation
Explaination1:
11 is represented as 1011 in binary.
"""

class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        ans = 0
        while A != 0:
            A = A & (A-1)
            ans = ans + 1
        return ans


solu = Solution()
array = [
    11 , # 3
    16 ,  # 1
]
for A in array:
    ans = solu.numSetBits(A)
    print("output for ",A," is ",ans)