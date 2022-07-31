class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        str = "1"*A
        str = str + "0"*B
        ans = 0
        for i in range(len(str)):
            ans += int(str[i]) * 1<<(len(str)-1 - i)
        return ans

solu = Solution()
array = [
    [3,2], # 28
    [2,3]  # 24
]
for A in array:
    ans = solu.solve(A[0],A[1])
    print("output for ",A," is ",ans)