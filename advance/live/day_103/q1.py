"""

DP intro
When to use  DP
Steps for DP

1. #n stairs
    Given n steps, In how many ways we can go from 0th to nth step
    Note - from ith step, we can directly go to (i+1)th step or (i+2)th step

    1 = 1
    2 = 2
    3 = 3
    4 = 5

    dp[i] = dp[i-1] + dp[i-2] + 3

2. sqrt()
 Minimum no of perfect sqaures required to make sum=N

 N = 6
    1**2, 1**2, 2**2

 N = 10
    3**2, 1**2

 N = 9
    3**2

 N = 12
    3**2, 1**2, 1**2, 1**2
"""
import sys

class Solution:
    def numSquares(self, n):
        # Base case: If n is a perfect square, return 1
        if int(n**0.5)**2 == n:
            return 1
        
        # Initialize the result to the maximum possible value
        result = sys.maxsize
        
        # Try every possible perfect square less than n
        for i in range(1, int(n**0.5) + 1):
            result = min(result, self.numSquares(n - i*i) + 1)
        
        return result
    def sum(self,n):
        return self.numSquares(n)
        # Create a list to store the minimum number of squares required for each number from 0 to n
        dp = [sys.maxsize] * (n + 1)
        # Base case: 0 requires 0 squares
        dp[0] = 0
        # Compute the minimum number of squares required for each number from 1 to n
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                # Update the minimum number of squares required if a smaller value is found
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]


    def steps(self,n):
        cache = {}
        cache[1] = 1
        cache[2] = 2
        ans = -1
        for i in range(3,n+1):
            cache[i] = cache[i-1] + cache[i-2]
        return cache[n]

if __name__ == "__main__":
    solu = Solution()
    array = [
        [6] ,
        [10] ,
        [9] ,
        [12] ,
    ]
    for A in array:
        ans = solu.sum(A[0])
        print("output for ",A," is ",ans)
# solu = Solution()
# array = [
#     [] , 
# ]
# for A in array:
#     ans = solu.solve(A[0],A[1])
#     print("output for ",A," is ",ans)

