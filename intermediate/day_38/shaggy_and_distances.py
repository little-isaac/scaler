"""
Problem Description
Shaggy has an array A consisting of N elements. We call a pair of distinct indices in that array a special if elements at those indices in the array are equal.

Shaggy wants you to find a special pair such that the distance between that pair is minimum. Distance between two indices is defined as |i-j|. If there is no special pair in the array, then return -1.



Problem Constraints
1 <= |A| <= 105



Input Format
The first and only argument is an integer array A.



Output Format
Return one integer corresponding to the minimum possible distance between a special pair.



Example Input
Input 1:

A = [7, 1, 3, 4, 1, 7]
Input 2:

A = [1, 1]


Example Output
Output 1:

 3
Output 2:

 1


Example Explanation
Explanation 1:

Here we have 2 options:
1. A[1] and A[4] are both 1 so (1,4) is a special pair and |1-4|=3.
2. A[0] and A[5] are both 7 so (0,5) is a special pair and |0-5|=5.
Therefore the minimum possible distance is 3. 
Explanation 2:

Only possibility is choosing A[1] and A[2].
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        mydict = {}
        ans = 1000000000
        c = 0
        for i in A:
            if i in mydict:
                ans = min(ans, c - mydict[i])
                mydict[i] = c
            else:
                mydict[i] = c
            c = c + 1
        if ans == 1000000000:
            ans = -1
        return ans

    def solveA(self, A):
        n = len(A)
        hashA = {}
        minDistance = -1
        prev = None
        for i in range(n):
            if prev is not None and A[i] == prev:
                return 1
            prev = A[i]
            if A[i] in hashA:
                indices = hashA[A[i]]
                for j in range(len(indices)):
                    dis = i - indices[j]
                    if dis < minDistance or minDistance == -1:
                        minDistance = dis
                hashA[A[i]].append(i)
            else:
                hashA[A[i]] = [i]
        return minDistance

solu = Solution()
array = [
    [[7, 1, 3, 4, 1, 7]] , # 3
    [[1, 1]] , # 1
]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)