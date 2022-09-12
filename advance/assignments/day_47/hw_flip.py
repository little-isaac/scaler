"""
Problem Description
You are given a binary string A(i.e., with characters 0 and 1) consisting of characters A1, A2, ..., AN. In a single operation, you can choose two indices, L and R, such that 1 ≤ L ≤ R ≤ N and flip the characters AL, AL+1, ..., AR. By flipping, we mean changing character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in the final string number of 1s is maximized.

If you don't want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.

NOTE: Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.



Problem Constraints
1 <= size of string <= 100000



Input Format
First and only argument is a string A.



Output Format
Return an array of integers denoting the answer.



Example Input
Input 1:

A = "010"
Input 2:

A = "111"


Example Output
Output 1:

[1, 1]
Output 2:

[]


Example Explanation
Explanation 1:

A = "010"

Pair of [L, R] | Final string
_______________|_____________
[1 1]          | "110"
[1 2]          | "100"
[1 3]          | "101"
[2 2]          | "000"
[2 3]          | "001"

We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return [1, 1].
Explanation 2:

No operation can give us more than three 1s in final string. So, we return empty array [].
"""

class Solution:
    # @param A : string
    # @return a list of integers
    def leftPsum(self,A):
        n = len(A)
        pf = [0]*n
        pf[0] = int(A[0])
        for i in range(1,n):
            pf[i] = pf[i-1] + int(A[i])
        return pf
    def leftRPsum(self,A):
        n = len(A)
        pf = [0]*n
        pf[0] = 0
        if int(A[0]) != 1:
            pf[0] = 1
        for i in range(1,n):
            c = 0
            if int(A[i]) != 1:
                c = 1
            if int(A[i]) == 1:
                pf[i] = c
            else:
                pf[i] = pf[i-1] + c
        return pf
    def rangeSum(self, l, r, pf):
        if l == 0:
            return pf[r]
        else:
            return pf[r] - pf[l-1]
    def flip(self, A):
        n = len(A)
        A = list(map(int, list(A)))
        count1 = 0
        for i in range(n):
            if A[i] == 1:
                count1 += 1
        if n == count1:
            return []
        numbers = [0] * n
        s = 0
        e = 0
        tS = 0
        sum = 0
        maximum = float("-inf")
        for i in range(n):
            if int(A[i]) == 0:
                numbers[i] = 1
            else:
                numbers[i] = -1
        for i in range(n):
            sum = sum + numbers[i]
            if sum < 0:
                sum = 0
                tS = i+1
            if maximum < sum:
                maximum = sum
                s = tS
                e = i

        return [s+1,e+1]

solu = Solution()
array = [
    ["010"], # [1, 1]
    ["111"], # []
    ["0011101"], # [1,2]
    ["1100010"], # [3,5]
    ["1101010001"], # [3,9]
    ]
for A in array:
    ans = solu.flip(A[0])
    print("output for ",A," is ",ans)