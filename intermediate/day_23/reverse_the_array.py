"""
Problem Description
You are given a constant array A.

You are required to return another array which is the reversed form of the input array.
"""

"""
Problem Constraints
1 <= A.size() <= 10000

1 <= A[i] <= 10000
"""

"""
Input Format
First argument is a constant array A.
"""

"""
Output Format
Return an integer array.
"""

"""
Example Input
Input 1:

A = [1,2,3,2,1]

Output 1:

[1,2,3,2,1] 


Input 2:

A = [1,1,10]

Output 2:

[10,1,1]
"""

"""
Example Explanation

Explanation 1:

Reversed form of input array is same as original array

Explanation 2:

Clearly, Reverse of [1,1,10] is [10,1,1]
"""

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def replaceArray(self,arr,s,e):
        i = s
        j = e
        while(i<j):
            arr[i],arr[j] = arr[j],arr[i]
            i = i + 1
            j = j - 1
        return arr

    def solve(self, A):
        return self.replaceArray(A,0,len(A)-1)

solu = Solution()
array = [
    [1,2,3,2,1],
    [1,1,10]
]
for A in array:
    ans = solu.solve(A)
    print("output for ",A," is ",ans)