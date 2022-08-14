"""
Problem Description
Given an array B of length A with elements 1 or 0. Find the number of subarrays with bitwise OR 1.


Problem Constraints
1 <= A <= 105


Input Format
The first argument is a single integer A.
The second argument is an integer array B.


Output Format
Return the number of subarrays with bitwise array 1.


Example Input
Input 1:
 A = 3
B = [1, 0, 1]
Input 2:
 A = 2
B = [1, 0]


Example Output
Output 1:
5
Output2:
2


Example Explanation
Explanation 1:
The subarrays are :- [1], [0], [1], [1, 0], [0, 1], [1, 0, 1]
Except the subarray [0] all the other subarrays has a Bitwise OR = 1
Explanation 2:
The subarrays are :- [1], [0], [1, 0]
Except the subarray [0] all the other subarrays has a Bitwise OR = 1
"""
class Solution:
    # @param A : integer
    # @param B : list of integers
     # @return an long
    def solve(self, A, B):
        n = A
        ans = 0
        for i in range(n):
            bitOr = B[i]
            for j in range(i,n):
                bitOr = bitOr | B[j]
                if bitOr == 1:
                    ans += 1
        return ans




solu = Solution()
array = [
    [3,[1, 0, 1]] , # 5
    [2, [1, 0]] , # 2
    [5, [ 0, 1, 1, 0, 1 ]] , # 13
]
for A in array:
    ans = solu.solve(A[0],A[1])
    print("output for ",A," is ",ans)