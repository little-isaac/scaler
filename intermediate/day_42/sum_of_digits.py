"""
Problem Description
Given a number A, we need to find the sum of its digits using recursion.



Problem Constraints
1 <= A <= 109



Input Format
The first and only argument is an integer A.



Output Format
Return an integer denoting the sum of digits of the number A.



Example Input
Input 1:

 A = 46
Input 2:

 A = 11


Example Output
Output 1:

 10
Output 2:

 2


Example Explanation
Explanation 1:

 Sum of digits of 46 = 4 + 6 = 10
Explanation 2:

 Sum of digits of 11 = 1 + 1 = 2
"""

class Solution:
    # @param A : integer
    # @return an integer
    def sumOfDigits(self,A,sum,i):
        sum = sum + int(str(A)[i])
        if i == len(str(A))-1:
            return sum
        return self.sumOfDigits(A,sum,i+1)
    def sumOfDigits(self,A):
        if A == 0: 
            return 0
        return (A % 10 + self.sumOfDigits(int(A / 10)))
    def solve(self, A):
        # return self.sumOfDigits(A,0,0)
        return self.sumOfDigits(A)


solu = Solution()
array = [
    [46] , # 10
    [11] , # 2
]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)