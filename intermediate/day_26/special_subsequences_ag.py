"""
Problem Description
You have given a string A having Uppercase English letters.

You have to find how many times subsequence "AG" is there in the given string.

NOTE: Return the answer modulo 109 + 7 as the answer can be very large.



Problem Constraints
1 <= length(A) <= 105



Input Format
First and only argument is a string A.



Output Format
Return an integer denoting the answer.



Example Input
Input 1:

 A = "ABCGAG"
Input 2:

 A = "GAB"


Example Output
Output 1:

 3
Output 2:

 0


Example Explanation
Explanation 1:

 Subsequence "AG" is 3 times in given string 
Explanation 2:

 There is no subsequence "AG" in the given string.
"""

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        ans = 0
        firstLetter = 'A'
        secondLetter = 'G'
        n = len(A)
        gc = 0
        ac = 0
        for i in range(n-1,-1,-1):
            char = A[i]
            if char == 'G':
                gc = gc + 1
            elif char == 'A':
                ans = ans + gc

        return ans % (1000000000+7)


solu = Solution()
array = [
    "ABCGAG", # 3
    "GAB",  # 0
]
for A in array:
    ans = solu.solve(A)
    print("output for ",A," is ",ans)