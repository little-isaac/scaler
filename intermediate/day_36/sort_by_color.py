"""
Problem Description
Given an array with N objects colored red, white, or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent red, white, and blue, respectively.

Note: Using the library sort function is not allowed.



Problem Constraints
1 <= N <= 1000000
0 <= A[i] <= 2


Input Format
First and only argument of input contains an integer array A.


Output Format
Return an integer array in asked order


Example Input
Input 1 :
    A = [0 1 2 0 1 2]
Input 2:

    A = [0]


Example Output
Output 1:
    [0 0 1 1 2 2]
Output 2:

    [0]


Example Explanation
Explanation 1:
    [0 0 1 1 2 2] is the required order.
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sortColorsHint(self, A):
        n = len(A)
        i = 0
        j = n - 1
        k = n - 1
        while i < k:
            if A[i] == 0:
                i += 1
            elif A[i] == 1:
                if i < j:
                    A[i],A[j] = A[j],A[i]
                    j-=1
                else:
                    i+= 1
            else:
                A[i],A[k] = A[k],A[i]
                k -= 1
                if j > k:
                    j = k
        return A
    def sortColors(self, A):
        n = len(A)
        count_0 = 0
        count_1 = 0
        count_2 = 0
        for i in range(n):
            if A[i] == 0:
                count_0 += 1
            elif A[i] == 1:
                count_1 += 1
            elif A[i] == 2:
                count_2 += 1
        return ('0' * count_0 + '1' * count_1 + '2' * count_2).strip()

solu = Solution()
array = [
    [[0, 1, 2, 0, 1, 2]] , # [0, 0, 1, 1, 2, 2]
    [[0]] , # [0]
]
for A in array:
    ans = solu.sortColors(A[0])
    print("output for ",A," is ",ans)