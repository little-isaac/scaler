"""
for each index find smaller element on the left side.
"""
from collections import deque

class Solution:
    def solve(self, A):
        n = len(A)
        stack = deque([])
        ans = [-1] * n
        stack.append(A[0])
        for i in range(1, n):
            while len(stack) > 0 and stack[-1] >= A[i]:
                stack.pop()
            if len(stack) > 0:
                ans[i] = stack[-1]
            stack.append(A[i])
        return ans



if __name__ == "__main__":
    sol = Solution()
    ans = sol.solve([5,2,8,10,6,1])
    print(ans)
    ans = sol.solve([5,2,8,10,6,1])
    print(ans)

