"""
Problem Description
Problem Description
Alex has a cat named Boomer. He decides to put his cat to the test for eternity.

He starts on day 1 with a stash of food unit, every next day, the stash doubles.

If Boomer is well behaved during a particular day, she receives food worth equal to the stash on that day.

Boomer receives a net worth of A units of food. What is the number of days he was well behaved?



Problem Constraints
1 <= A <= 231-1



Input Format
First and only argument is an integer A.



Output Format
Return an integer denoting the number of days Boomer was well behaved.



Example Input
Input 1:

A = 5
Input 2:

A = 8


Example Output
Output 1:

 2
Output 2:

 1


Example Explanation
Explanation 1:

 To eat a total of 5 units of food, Boomer behaved normally on Day 1 and on the Day 3.
Explanation 2:

 To eat a total of 8 units of food, Boomer behaved normally only on day 4.
"""

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        ans = 0
        while A!=0:
            if A&1 == 1:
                ans += 1
            A = A>>1
        return ans

solu = Solution()
array = [
    [5] , # 2
    [3] , # 2
    [7] , # 2
    [8] , # 1
    [111111111] , #18
]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)