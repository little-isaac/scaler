"""
You are given a string S, and you have to find all the amazing substrings of S.

An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).

Input

Only argument given is string S.
Output

Return a single integer X mod 10003, here X is the number of Amazing Substrings in given the string.
Constraints

1 <= length(S) <= 1e6
S can have special characters
Example

Input
    ABEC

Output
    6

Explanation
    Amazing substrings of given string are :
    1. A
    2. AB
    3. ABE
    4. ABEC
    5. E
    6. EC
    here number of substrings are 6 and 6 % 10003 = 6.
"""

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        ans = 0
        elemsToCheck = ['a','e','i','o','u','A','E','I','O','U']
        counter = 0
        for i in range(n-1,-1,-1):
            ele = A[i]
            counter = counter + 1
            if ele in elemsToCheck:
                ans = ans + counter
        return ans % 10003


solu = Solution()
array = [
    "ABEC", # 6
    "ABECDEPLQURTUPDLHFKLPWSHHFKGL", #117
]
for A in array:
    ans = solu.solve(A)
    print("output for ",A," is ",ans)