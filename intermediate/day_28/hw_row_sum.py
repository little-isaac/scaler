class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        m = len(A[0])
        ans = []
        for i in range(n):
            sum  = 0
            for j in range(m):
                sum += A[i][j]
            ans.append(sum)
        return ans


solu = Solution()
array = [
    [[[1,2,3,4],[5,6,7,8],[9,2,3,4]]] , # [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)