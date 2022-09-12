"""
Problem Description
Given an array A of N integers.

Find the largest continuous sequence in a array which sums to zero.



Problem Constraints
1 <= N <= 106

-107 <= A[i] <= 107



Input Format
Single argument which is an integer array A.



Output Format
Return an array denoting the longest continuous sequence with total sum of zero.

NOTE : If there are multiple correct answers, return the sequence which occurs first in the array.



Example Input
A = [1,2,-2,4,-4]


Example Output
[2,-2,4,-4]


Example Explanation
[2,-2,4,-4] is the longest sequence with total sum of zero.
"""

class Solution:
	# @param A : list of integers
	# @return a list of integers
    def pSum(self,A):
        n = len(A)
        pf = [0] * n
        pf[0] = A[0]
        for i in range(1,n):
            pf[i] = pf[i-1] + A[i]
        return pf

    def lszero(self, A):
        n = len(A)
        pf = self.pSum(A)
        hashA = {}
        maxLen = -1
        start = -1
        end = -1
        for i in range(n):
            if pf[i] == 0:
                tLen = i
                if tLen > maxLen or maxLen == -1:
                    maxLen = tLen
                    end = i
                    start = -1
            if pf[i] in hashA:
                tLen = i - hashA[pf[i]]
                if tLen > maxLen or maxLen == -1:
                    maxLen = tLen
                    end = i
                    start = hashA[pf[i]]
            else:
                hashA[pf[i]] = i
        start += 1
        end += 1
        return A[start:end]

solu = Solution()
array = [
    [[1,2,-2,4,-4]] , # [2,-2,4,-4]
    [[1,1,-2,1,-1]] , # [2,-2,4,-4]
    [[2,2,1,-3,4,3,1,-2,-3,2]] , # [2,-2,4,-4]
]
for A in array:
    ans = solu.lszero(A[0])
    print("output for ",A," is ",ans)