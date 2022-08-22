"""
There are certain problems which are asked in the interview to also check how you take care of overflows in your problem.
This is one of those problems.
Please take extra care to make sure that you are type-casting your ints to long properly and at all places. Try to verify if your solution works if number of elements is as large as 105

Food for thought :

Even though it might not be required in this problem, in some cases, you might be required to order the operations cleverly so that the numbers do not overflow.
For example, if you need to calculate n! / k! where n! is factorial(n), one approach is to calculate factorial(n), factorial(k) and then divide them.
Another approach is to only multiple numbers from k + 1 ... n to calculate the result.
Obviously approach 1 is more susceptible to overflows.
You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4
"""

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumberTwo(self, A):
        sumOfA = 0
        sumOfA2 = 0
        n = 0
        for a in A:
            sumOfA2 += a*a
            sumOfA += a
            n += 1
        sumOfN = n*(n+1)/2
        retA = sumOfN - sumOfA
        retB = (sumOfN*(2*n+1)/3 - sumOfA2)/retA
        x = (retB-retA)/2
        return [x,x + retA]
    def repeatedNumber(self, A):
        n = len(A)
        repeated = 0
        missing = 0
        for i in range(n):
            index = A[i]
            if index < 0:
                index *= -1
            index -= 1
            if A[index] > 0:
                A[index] = A[index] * -1
            else:
                if A[i] < 0:
                    repeated = A[i] * -1
                else:
                    repeated = A[i]
        for i in range(n):
            if A[i] > 0:
                missing = i + 1
        return repeated,missing


solu = Solution()
array = [
    [3, 1, 2, 5, 3] , # [3,4]
    [2,3,4,5,2] , # [2,1]
    [ 5, 2, 5, 3, 4, 7, 1 ] , # [2,1]
]
for A in array:
    ans = solu.repeatedNumberTwo(A)
    print("output for ",A," is ",ans)