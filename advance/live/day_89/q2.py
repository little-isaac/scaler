"""
Given continues blocks of histograms, find max rectangular area.
Not: every historgram has a width of 1

ar[6] = [2,4,3,4,5,1] = 12


find first smaller element from left and right and calcuulate area.
and find maximum from that
"""

from collections import deque

class Solution:
    def smallerLeft(self, A):
        n = len(A)
        stack = deque([])
        ans = [-1] * n
        stack.append(0)
        for i in range(1, n):
            while len(stack) > 0 and A[stack[-1]] >= A[i]:
                stack.pop()
            if len(stack) > 0:
                ans[i] = stack[-1]
            stack.append(i)
        return ans

    def smallerRight(self, A):
        n = len(A)
        stack = deque([])
        ans = [-1] * n
        stack.append(n-1)
        for i in range(n-2, -1, -1):
            # print(stack,i,A[i])
            while len(stack) > 0 and A[stack[-1]] >= A[i]:
                stack.pop()
            if len(stack) > 0:
                ans[i] = stack[-1]
            stack.append(i)
        return ans
    def solve(self, A):
        n = len(A)
        left = self.smallerLeft(A)
        right = self.smallerRight(A)
        ans = 0
        for i in range(n):
            leftMin = left[i]
            rightMin = right[i]
            if rightMin == -1:
                rightMin = n
            distance = rightMin - leftMin - 1
            area = distance * A[i]
            ans = max(ans,area)
        return ans


if __name__ == "__main__":
    sol = Solution()
    ans = sol.solve([5,2,8,10,6,1])
    print(ans)
    ans = sol.solve([5,2,8,10,6,1])
    print(ans)
    ans = sol.solve([4,3,4])
    print(ans)
