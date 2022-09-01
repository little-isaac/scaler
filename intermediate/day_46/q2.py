class Solution:

        def solve(self, A):
            if A == 0:
                return 1
            if A == 1:
                return 1
            if A == 2:
                return 2
            return self.solve(A-1) + self.solve(A-2) + self.solve(A-3) + A


solu = Solution()
array = [
    [3] , # 7
    [2] , # 2
    [19] , # 163451
]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)

# python3 intermediate/day_46/q2.py