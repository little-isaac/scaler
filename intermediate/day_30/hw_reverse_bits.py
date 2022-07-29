"""
Problem Description
Reverse the bits of an 32 bit unsigned integer A.



Problem Constraints
0 <= A <= 232



Input Format
First and only argument of input contains an integer A.



Output Format
Return a single unsigned integer denoting the decimal value of reversed bits.



Example Input
Input 1:

 0
Input 2:

 3


Example Output
Output 1:

 0
Output 2:

 3221225472


Example Explanation
Explanation 1:

        00000000000000000000000000000000    
=>      00000000000000000000000000000000
Explanation 2:

        00000000000000000000000000000011    
=>      11000000000000000000000000000000
"""
class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def setIBit(self,a,i):
        return a | 1<<i
    def isBitSet(self,a,i):
        return ((a>>i)&1) == 1
    def reverse(self, A):
        length = 31
        a = 0
        counter = 0
        while(A > 0):
            if A&1 == 1:
                a = self.setIBit(a,length - counter)
            counter += 1
            A = A >> 1
        return a





solu = Solution()
array = [
    [0] , # 0
    [3] ,  # 3221225472
    [2] ,  # 3221225472
]
for A in array:
    ans = solu.reverse(A[0])
    print("output for ",A," is ",ans)