"""
Problem Description
Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array

and at least one occurrence of the minimum value of the array.



Problem Constraints
1 <= |A| <= 2000



Input Format
First and only argument is vector A



Output Format
Return the length of the smallest subarray which has at least one occurrence of minimum and maximum element of the array



Example Input
Input 1:

A = [1, 3]
Input 2:

A = [2]


Example Output
Output 1:

 2
Output 2:

 1


Example Explanation
Explanation 1:

 Only choice is to take both elements.
Explanation 2:

 Take the whole array.
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        mini = min(A)
        maxi = max(A)
        if mini == maxi:
            return 1
        minIndex = -1
        maxIndex = -1
        ans = n
        for i in range(n-1,-1,-1):
            ele = A[i]
            if ele == mini:
                minIndex = i
                if maxIndex != -1:
                    length = maxIndex - minIndex + 1
                    ans = min(ans,length)
            elif ele == maxi:
                maxIndex = i
                if minIndex != -1:
                    length = minIndex - maxIndex + 1
                    ans = min(ans,length)
        return ans

solu = Solution()
array = [
    [1, 3], # 3
    [2],  # 0
    [2,2,6,4,5,1,5,6,2,4,3,4,1] #3
]
for A in array:
    ans = solu.solve(A)
    print("output for ",A," is ",ans)