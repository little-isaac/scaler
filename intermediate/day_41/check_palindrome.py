"""
Problem Description
Write a recursive function that checks whether string A is a palindrome or Not.
Return 1 if the string A is a palindrome, else return 0.

Note: A palindrome is a string that's the same when read forward and backward.



Problem Constraints
1 <= |A| <= 50000

String A consists only of lowercase letters.



Input Format
The first and only argument is a string A.



Output Format
Return 1 if the string A is a palindrome, else return 0.



Example Input
Input 1:

 A = "naman"
Input 2:

 A = "strings"


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 "naman" is a palindomic string, so return 1.
Explanation 2:

 "strings" is not a palindrome, so return 0.
"""

import sys
sys.setrecursionlimit(10**6)

class Solution:
    # @param A : string
    # @return an integer
    def isPalindrom(self,A,i,j):
        if A[i] != A[j]:
            return 0
        if i >= j:
            return 1
        return self.isPalindrom(A,i+1,j-1)

    def solve(self, A):
        return self.isPalindrom(A,0,len(A)-1)



solu = Solution()
array = [
    ["naman"] , # 1
    ["naan"] , # 1
    ["nqan"] , # 1
    ["strings"] , # 0
]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)