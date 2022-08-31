"""
Given a binary string A. It is allowed to do at most one swap between any 0 and 1. Find and return the length of the longest consecutive 1’s that can be achieved.


Input Format

The only argument given is string A.
Output Format

Return the length of the longest consecutive 1’s that can be achieved.
Constraints

1 <= length of string <= 1000000
A contains only characters 0 and 1.
For Example

Input 1:
    A = "111000"
Output 1:
    3

Input 2:
    A = "111011101"
Output 2:
    7
"""

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        A = list(A)
        n = len(A)
        countOf1 = 0
        for i in range(n):
            if A[i] == '1':
                countOf1 += 1
        if countOf1 == n:
            return n
        ans = 0
        for i in range(n):
            if A[i] == '1':
                continue
            l = 0
            for j in range(i-1,-1,-1):
                if A[j] == '1':
                    l += 1
                else:
                    break
            r = 0
            for j in range(i+1,n):
                if A[j] == '1':
                    r += 1
                else:
                    break
            ones = 0
            if (l + r) == countOf1:
                ones = l + r
            else:
                ones = l + r + 1
            ans = max(ans,ones)
        return ans



solu = Solution()
array = [
    ["111000"] , # 3
    ["111011101"] ,  # 7
]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)