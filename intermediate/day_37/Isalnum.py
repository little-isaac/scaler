"""
Problem Description
You are given a function isalpha() consisting of a character array A.

Return 1 if all the characters of a character array are alphanumeric (a-z, A-Z, and 0-9) else, return 0.



Problem Constraints
1 <= |A| <= 105



Input Format
Only argument is a character array A.



Output Format
Return 1 if all the characters of the character array are alphanumeric (a-z, A-Z and 0-9), else return 0.



Example Input
Input 1:

 A = ['S', 'c', 'a', 'l', 'e', 'r', 'A', 'c', 'a', 'd', 'e', 'm', 'y', '2', '0', '2', '0']
Input 2:

 A = ['S', 'c', 'a', 'l', 'e', 'r', '#', '2', '0', '2', '0']


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 All the characters are alphanumeric.
Explanation 2:

 All the characters are NOT alphabets i.e ('#').
"""

class Solution:
    # @param A : list of characters
    # @return a list of characters
    def isInSmallCase(self,char):
        sS = ord('a')
        sE = ord('z')
        aci = ord(char)
        return aci <= sE and aci >= sS

    def isInCapitalCase(self,char):
        cS = ord('A')
        cE = ord('Z')
        aci = ord(char)
        return aci <= cE and aci >= cS

    def isInDigitCase(self,char):
        dS = ord('0')
        dE = ord('9')
        aci = ord(char)
        return aci <= dE and aci >= dS

    def solve(self, A):
        n = len(A)
        for i in range(n):
            if self.isInDigitCase(A[i]) != True and self.isInCapitalCase(A[i]) != True and self.isInSmallCase(A[i]) != True:
                return 0
        return 1

solu = Solution()
array = [
    [['S', 'c', 'a', 'l', 'e', 'r', 'A', 'c', 'a', 'd', 'e', 'm', 'y', '2', '0', '2', '0']] , # 1
    [['S', 'c', 'a', 'l', 'e', 'r', '#', '2', '0', '2', '0']] , # 0
]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)