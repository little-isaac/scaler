"""
Groot has N trees lined up in front of him where the height of the i'th tree is denoted by H[i].

He wants to select some trees to replace his broken branches.

But he wants uniformity in his selection of trees.

So he picks only those trees whose heights have frequency B.

He then sums up the heights that occur B times. (He adds the height only once to the sum and not B times).

But the sum he ended up getting was huge so he prints it modulo 10^9+7.

In case no such cluster exists, Groot becomes sad and prints -1.

Constraints:

1.   1<=N<=100000
2.   1<=B<=N
3.   0<=H[i]<=10^9
Input: Integers N and B and an array C of size N

Output: Sum of all numbers in the array that occur exactly B times.

Example:

Input:

N=5 ,B=2 ,C=[1 2 2 3 3]
Output:

5
Explanation:

There are 3 distinct numbers in the array which are 1,2,3.
Out of these, only 2 and 3 occur twice. Therefore the answer is sum of 2 and 3 which is 5.
"""

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def getSum(self, N, B, A):
        hashA = {}
        for i in range(N):
            if A[i] in hashA:
                hashA[A[i]] += 1
            else:
                hashA[A[i]] = 1
        sum = 0
        isFound = False
        for ele in hashA:
            if hashA[ele] == B:
                isFound = True
                sum = sum + ele
        if isFound:
            return sum % (10**9+7)
        return -1


solu = Solution()
array = [
    [5,2,[1,2,2,3,3]] , # 5
    [6,2,[ 1000000000, 1000000000, 999999999, 999999999, 999999998, 1 ]] , # 999999992
]
for A in array:
    ans = solu.getSum(A[0],A[1],A[2])
    print("output for ",A," is ",ans)