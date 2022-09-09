class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        ans = 0
        A.sort(reverse=True)
        for i in range(n):
            ele = A[i]
            ans += (ele * (i+1))
        return ans



solu = Solution()
array = [
    [[2, 1]] , # 4
    [[5]] , # 5
]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)