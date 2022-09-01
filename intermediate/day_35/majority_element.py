"""
Problem Description
Given an array of size N, find the majority element. The majority element is the element that appears more than floor(n/2) times.
You may assume that the array is non-empty and the majority element always exists in the array.



Problem Constraints
1 <= N <= 5*105
1 <= num[i] <= 109


Input Format
Only argument is an integer array.


Output Format
Return an integer.


Example Input
[2, 1, 2]


Example Output
2


Example Explanation
2 occurs 2 times which is greater than 3/2.
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        n = len(A)
        ele = A[0]
        fre = 1
        for i in range(1,n):
            if ele == -1:
                ele = A[i]
                fre = 1
            elif A[i] == ele:
                fre += 1
            else:
                fre -= 1

            if fre == 0:
                ele = -1
        return ele


solu = Solution()
array = [
    [[2, 1, 2]] , # 2
]
for A in array:
    ans = solu.majorityElement(A[0])
    print("output for ",A," is ",ans)