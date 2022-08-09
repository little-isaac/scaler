"""
Problem Description
Given a string A of size N, find and return the longest palindromic substring in A.

Substring of string A is A[i...j] where 0 <= i <= j < len(A)

Palindrome string:
A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.

Incase of conflict, return the substring which occurs first ( with the least starting index).



Problem Constraints
1 <= N <= 6000



Input Format
First and only argument is a string A.



Output Format
Return a string denoting the longest palindromic substring of string A.



Example Input
A = "aaaabaaa"


Example Output
"aaabaaa"


Example Explanation
We can see that longest palindromic substring is of length 7 and the string is "aaabaaa".
"""

class Solution:
	# @param A : string
	# @return a strings
    def getPoints(self,A,s,e):
        n = len(A)
        while s > -1 and e < n and A[s] == A[e]:
                s -= 1
                e += 1
        return s,e

    def longestPalindrome(self, strA):
        A = list(strA)
        n = len(A)
        ans = 0
        s = 0
        e = 0
        ansA = []
        for i in range(n):
            x,y = self.getPoints(A,i,i)
            strLength = y-x-1
            if strLength > ans:
                s = x+1
                e = y-1
                ans = strLength

            ans = max(ans,strLength)

            x,y = self.getPoints(A,i,i+1)
            strLength = y-x-1
            if strLength > ans:
                s = x+1
                e = y-1
                ans = strLength

        for i in range(s,e+1):
            ansA.append(A[i])

        return "".join(ansA)



solu = Solution()
array = [
    ["aaaabaaa"] , # "aaabaaa"
    ["abccba"] , # "abccba"
    ["madam"] , # "madam"
]
for A in array:
    ans = solu.longestPalindrome(A[0])
    print("output for ",A," is ",ans)