"""
Problem Description
Given the array of strings A, you need to find the longest string S, which is the prefix of ALL the strings in the array.

The longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.

Example: the longest common prefix of "abcdefgh" and "abcefgh" is "abc".



Problem Constraints
0 <= sum of length of all strings <= 1000000



Input Format
The only argument given is an array of strings A.



Output Format
Return the longest common prefix of all strings in A.



Example Input
Input 1:

A = ["abcdefgh", "aefghijk", "abcefgh"]
Input 2:

A = ["abab", "ab", "abcd"];


Example Output
Output 1:

"a"
Output 2:

"ab"


Example Explanation
Explanation 1:

Longest common prefix of all the strings is "a".
Explanation 2:

Longest common prefix of all the strings is "ab".
"""
class Solution:
	# @param A : list of strings
	# @return a strings
    def longestCommonPrefix(self, A):
        n = len(A)
        minimumLength = len(A[0])
        for i in range(n):
            minimumLength = min(minimumLength,len(A[i]))
        isLetterChanged = False
        counter = 0
        ans = []
        while isLetterChanged == False:
            currentLetter = A[0][counter]
            # print(counter,currentLetter)
            for i in range(1,n):
                if A[i][counter] != currentLetter:
                    isLetterChanged = True
                    break
            if isLetterChanged == False:
                ans.append(currentLetter)
            counter += 1
            if counter >= minimumLength:
                isLetterChanged = True
        return "".join(ans)


solu = Solution()
array = [
    [["abcdefgh", "aefghijk", "abcefgh"]] , # "a"
    [["abab", "ab", "abcd"]] , # "ab"
]
for A in array:
    ans = solu.longestCommonPrefix(A[0])
    print("output for ",A," is ",ans)