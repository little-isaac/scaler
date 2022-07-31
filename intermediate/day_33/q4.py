class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        ans = 0
        isFound = False
        n = len(A)
        for ele in A:
            if ele == B:
                isFound = True
            if ele > B:
                ans += 1
        if isFound:
            return ans
        else:
            return -1

solu = Solution()
array = [
    [[2, 4, 3, 1, 5],3], # 3
    [[1,4,2],3]  # -1
]
for A in array:
    ans = solu.solve(A[0],A[1])
    print("output for ",A," is ",ans)