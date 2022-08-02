class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A[0])
        sum = 0
        for i in range(n):
            sum += A[i][i]
        return sum

solu = Solution()
array = [
    [[[1, -2, -3], [-4, 5, -6], [-7, -8, 9]]] , # 15
    [[[3, 2], [2, 3]]] , # 6
]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)