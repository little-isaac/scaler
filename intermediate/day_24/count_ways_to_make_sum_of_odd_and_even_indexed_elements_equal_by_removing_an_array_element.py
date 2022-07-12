"""
Problem Description
Given an array, arr[] of size N, the task is to find the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.



Problem Constraints
1 <= n <= 105
-105 <= A[i] <= 105


Input Format
First argument contains an array A of integers of size N


Output Format
Return the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.



Example Input
Input 1:
A=[2, 1, 6, 4]
Input 2:

A=[1, 1, 1]


Example Output
Output 1:
1
Output 2:

3


Example Explanation
Explanation 1:
Removing arr[1] from the array modifies arr[] to { 2, 6, 4 } such that, arr[0] + arr[2] = arr[1]. 
Therefore, the required output is 1. 
Explanation 2:

Removing arr[0] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Removing arr[1] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Removing arr[2] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Therefore, the required output is 3.

"""

class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
    ODD = 1
    EVEN = 0
    def getPrefixSum(self,A,type):
        n = len(A)
        pf = [0] * n
        for i in range(0,n):
            if type == self.EVEN:
                if i % 2 == 0:
                    pf[i] = pf[i-1] + A[i]
                else:
                    pf[i] = pf[i-1]
            elif type == self.ODD:
                if i % 2 == 0:
                    if i != 0:
                        pf[i] = pf[i-1]
                    else:
                        pf[i] = 0
                else:
                    pf[i] = pf[i-1] + A[i]
        return pf
    def solve(self,A):
        n = len(A)
        pfEven = [0] * n
        pfOdd = [0] * n
        pfEven = self.getPrefixSum(A,self.EVEN)
        pfOdd = self.getPrefixSum(A,self.ODD)
        count = 0
        for i in range(0,n):
            sumEven = 0
            sumOdd = 0
            if i == 0:
                sumEven = 0
                sumOdd = 0
            else:
                sumEven = self.rangeSum(0,i-1,pfEven)
                sumOdd = self.rangeSum(0,i-1,pfOdd)
            sumEven = sumEven + self.rangeSum(i+1,n-1,pfOdd)
            sumOdd = sumOdd + self.rangeSum(i+1,n-1,pfEven)
            if sumEven == sumOdd:
                count = count + 1
        return count

    def rangeSum(self, l, r, pf):
        if l == 0:
            return pf[r]
        else:
            return pf[r] - pf[l-1]

solu = Solution()
array = [
    [3,4,-2,8,6,2,1,3],
    [4,3,2,7,6,-2],
    [4,1,5,3,7,10],
    [2, 1, 6, 4], # 1
    [1, 1, 1]  # 3
]
for A in array:
    ans = solu.solve(A)
    print("output for ",A," is ",ans)