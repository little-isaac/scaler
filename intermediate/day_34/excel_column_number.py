"""
Problem Description
Given a column title as appears in an Excel sheet, return its corresponding column number.



Problem Constraints
1 <= length of the column title <= 5



Input Format
The only argument is a string that represents the column title in the excel sheet.



Output Format
Return a single integer that represents the corresponding column number.



Example Input
Input 1:

 AB
Input 2:

 BB


Example Output
Output 1:

 28
Output 2:

 54


Example Explanation
Explanation 1:

 A -> 1
 B -> 2
 C -> 3
 ...
 Z -> 26
 AA -> 27
 AB -> 28
Explanation 2:

 A -> 1
 B -> 2
 C -> 3
 ...
 Z -> 26
 AA -> 27
 AB -> 28
 ...
 AZ -> 52
 BA -> 53
 BB -> 54
"""
class Solution:
	# @param A : string
	# @return an integer
    def getCode(self,c):
        return ord(c) - 64
    def titleToNumber(self, A):
        ans = 0
        mul = 1
        n = len(A)
        for i in range(n-1,-1,-1):
            ele = A[i]
            code = self.getCode(ele)
            ans += code * (mul)
            mul *= 26
        return ans

solu = Solution()
array = [
    ["A"] , # 1
    ["Z"] , # 26
    ["AB"] , # 28
    ["BA"] , # 53
    ["ABA"] , # 729
]
for A in array:
    ans = solu.titleToNumber(A[0])
    print("output for ",A," is ",ans)