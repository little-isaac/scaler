"""
Problem Description
You are given an integer array C of size A. Now you need to find a subarray (contiguous elements) so that the sum of contiguous elements is maximum.
But the sum must not exceed B.


Problem Constraints
1 <= A <= 103
1 <= B <= 109
1 <= C[i] <= 106


Input Format
The first argument is the integer A.
The second argument is the integer B.
The third argument is the integer array C.


Output Format
Return a single integer which denotes the maximum sum.


Example Input
Input 1:
A = 5
B = 12
C = [2, 1, 3, 4, 5]
Input 2:

A = 3
B = 1
C = [2, 2, 2]


Example Output
Output 1:
12
Output 2:

0


Example Explanation
Explanation 1:
We can select {3,4,5} which sums up to 12 which is the maximum possible sum.
Explanation 2:

All elements are greater than B, which means we cannot select any subarray.
Hence, the answer is 0.
"""

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def maxSubarray(self, A, B, C):
        ans = 0
        for i in range(A):
            sum = 0
            for j in range(i,A):
                sum += C[j]
                if sum > B:
                    continue
                ans = max(ans,sum)
            # ans = max(ans,sum)
        return ans



solu = Solution()
array = [
    [5,12,[2, 1, 3, 4, 5]] , # 12
    [3,1,[2, 2, 2]] ,  # 0
]
for A in array:
    ans = solu.maxSubarray(A[0],A[1],A[2])
    print("output for ",A," is ",ans)