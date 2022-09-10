"""
Problem Description
Find the contiguous non-empty subarray within an array, A of length N, with the largest sum.



Problem Constraints
1 <= N <= 1e6
-1000 <= A[i] <= 1000



Input Format
The first and the only argument contains an integer array, A.



Output Format
Return an integer representing the maximum possible sum of the contiguous subarray.



Example Input
Input 1:

 A = [1, 2, 3, 4, -10] 
Input 2:

 A = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 


Example Output
Output 1:

 10 
Output 2:

 6 


Example Explanation
Explanation 1:

 The subarray [1, 2, 3, 4] has the maximum possible sum of 10. 
Explanation 2:

 The subarray [4,-1,2,1] has the maximum possible sum of 6. 
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        n = len(A)
        ans = float("-inf")
        sum = 0
        for i in range(n):
            sum += A[i]
            ans = max(ans,sum)
            if sum < 0:
                sum = 0
        return ans

    def maxSubArray(self, A):
        n = len(A)
        ans = 0
        for i in range(n):
            sum = 0
            for j in range(i,n):
                sum += A[j]
                ans = max(ans,sum)
        return ans


solu = Solution()
array = [
    [[1, 2, 3, 4, -10] ], # 10
    [[-2, 1, -3, 4, -1, 2, 1, -5, 4]], # 6
    ]
for A in array:
    ans = solu.maxSubArray(A[0])
    print("output for ",A," is ",ans)