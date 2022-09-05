"""
Problem Description
Given an array of integers A, of size N.

Return the maximum size subarray of A having only non-negative elements. If there are more than one such subarray, return the one having the smallest starting index in A.

NOTE: It is guaranteed that an answer always exists.



Problem Constraints
1 <= N <= 105

-109 <= A[i] <= 109



Input Format
The first and only argument given is the integer array A.



Output Format
Return maximum size subarray of A having only non-negative elements. If there are more than one such subarrays, return the one having earliest starting index in A.



Example Input
Input 1:

 A = [5, 6, -1, 7, 8]
Input 2:

 A = [1, 2, 3, 4, 5, 6]


Example Output
Output 1:

 [5, 6]
Output 2:

 [1, 2, 3, 4, 5, 6]


Example Explanation
Explanation 1:

 There are two subarrays of size 2 having only non-negative elements.
 1. [5, 6]  starting point  = 0
 2. [7, 8]  starting point  = 3
 As starting point of 1 is smaller, return [5, 6]
Explanation 2:

 There is only one subarray of size 6 having only non-negative elements:
 [1, 2, 3, 4, 5, 6]
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        start = -1
        end = -1
        maxLen = 0
        indexes = []
        for i in range(n):
            ele = A[i]
            if ele < 0:
                start = i
                end = i
            else:
                end = i
            diff = end - start
            # print(i,start,end,diff)
            if maxLen < diff:
                indexes = [start,end]
                maxLen = diff
        return A[indexes[0]+1:indexes[1]+1]





solu = Solution()
array = [
    [[5, 6, -1, 7, 8]] , # [5, 6]
    [[1, 2, 3, 4, 5, 6]] ,  # [1, 2, 3, 4, 5, 6]
    [[ 8986143, -5026827, 5591744, 4058312, 2210051, 5680315, -5251946, -607433, 1633303, 2186575 ]] ,  # [5591744,4058312,2210051,5680315 ]
    [[ -3674875, 5305422, 7665178, 205505, -7168198, -1398091, 5392310, -1700856, 1259052, -3056006 ]] ,  # [5305422,7665178,205505]
    [[ -5173778, -8176176, 1694510, 7089884, -1394259, 1146372, -2502339, 1544618, 6602022, 4330572 ]], # [1544618, 6602022, 4330572]
    [[ -4549634, -3196682, 8455838, -1432628, -263819, -3928366, -5556259, -2114783, 3923939, -4183708 ]], # [8455838]
]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A[0]," is ",ans)