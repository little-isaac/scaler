class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A[0])
        sum = 0
        for i in range(n-1,-1,-1):
            sum += A[n-i-1][i]
        return sum

solu = Solution()
array = [
    [[[1, -2, -3], [-4, 5, -6], [-7, -8, 9]]] , # -5
    [[[3, 2], [2, 3]]] , # 4
]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)