"""
Problem Description
Given a string A consisting of lowercase characters.

Check if characters of the given string can be rearranged to form a palindrome.

Return 1 if it is possible to rearrange the characters of the string A such that it becomes a palindrome else return 0.



Problem Constraints
1 <= |A| <= 105

A consists only of lower-case characters.



Input Format
First argument is an string A.



Output Format
Return 1 if it is possible to rearrange the characters of the string A such that it becomes a palindrome else return 0.



Example Input
Input 1:

 A = "abcde"
Input 2:

 A = "abbaee"


Example Output
Output 1:

 0
Output 2:

 1


Example Explanation
Explanation 1:

 No possible rearrangement to make the string palindrome.
Explanation 2:

 Given string "abbaee" can be rearranged to "aebbea" to form a palindrome.
"""

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        A = list(A)
        hashA = {}
        for i in range(n):
            if A[i] not in hashA:
                hashA[A[i]] = 1
            else:
                hashA[A[i]] += 1
        isEvenLen = n & 1 == 0
        isOddFound = False
        for ele in hashA:
            if hashA[ele] & 1 == 1:
                if isOddFound is False:
                    isOddFound = True
                else:
                    return 0
        return 1


                

solu = Solution()
array = [
    ["abcde"] , # 0
    ["abbaee"] , # 1
]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)