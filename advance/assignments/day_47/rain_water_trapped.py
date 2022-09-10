"""
Problem Description
Given a vector A of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.



Problem Constraints
1 <= |A| <= 100000



Input Format
First and only argument is the vector A



Output Format
Return one integer, the answer to the question



Example Input
Input 1:

A = [0, 1, 0, 2]
Input 2:

A = [1, 2]


Example Output
Output 1:

1
Output 2:

0


Example Explanation
Explanation 1:

1 unit is trapped on top of the 3rd element.
Explanation 2:

No water is trapped.
"""

class Solution:
	# @param A : tuple of integers
	# @return an integer
    def getPFM(self,A):
        n = len(A)
        pfm = []
        pfm.append(A[0])
        for i in range(1,n):
            if A[i] < pfm[i-1]:
                pfm.append(pfm[i-1])
            else:
                pfm.append(A[i])
        return pfm
    def getSFM(self,A):
        n = len(A)
        sfm = [0]*n
        sfm[n-1] = A[n-1]
        for i in range(n-2,-1,-1):
            if A[i] < sfm[i+1]:
                sfm[i] = sfm[i+1]
            else:
                sfm[i] = A[i]
        return sfm

    def trap(self, A):
        n = len(A)
        pfm = self.getPFM(A)
        sfm = self.getSFM(A)
        ans = 0
        for i in range(1,n-1):
            leftMax = pfm[i-1]
            rightMax = sfm[i+1]
            level = min(leftMax,rightMax)
            # if the m is small then A[i] then it means we cannot store water
            # print(i,A[i],level,level-A[i])
            diff = level-A[i]
            if diff > 0:
                ans += diff
        return ans

solu = Solution()
array = [
    [[2,1,3,2,1,2,4,3,2,1,3,1]], # 8
    [[10,7,3,5,2,3,6,9,8,11]], # 37
    [[4,2,5,7,4,2,3,6,8,2,3]], # 16
    ]
for A in array:
    ans = solu.trap(A[0])
    print("output for ",A," is ",ans)