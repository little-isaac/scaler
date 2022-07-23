"""
Problem Description
Given two binary strings, return their sum (also a binary string).
Example:

a = "100"

b = "11"
Return a + b = "111".
"""

class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
    def binToDeci(self,a):
        return int(a,2)

    def deciToBin(self,a):
        return bin(a).replace('0b','')

    def addBinary(self, A, B):
        a = self.binToDeci(A)
        b = self.binToDeci(B)
        return self.deciToBin(a+b)

solu = Solution()
array = [
    ["100","11"] , # 111
    ["101","010"] ,  # 111
]
for A in array:
    ans = solu.addBinary(A[0],A[1])
    print("output for ",A," is ",ans)