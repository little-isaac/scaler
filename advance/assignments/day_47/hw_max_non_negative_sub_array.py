class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        n = len(A)
        maxSum = float("-inf")
        sum = 0
        ans = []
        temp = []
        for i in range(n):
            if A[i] < 0:
                sum = 0
                temp = []
                continue
            sum += A[i]
            temp.append(A[i])
            if sum > maxSum:
                maxSum = sum
                ans = temp
        return ans

solu = Solution()
array = [
    [[1, 2, 5, -7, 2, 3]], #[1, 2, 5]
    [[10, -1, 2, 3, -4, 100]] # [100]
    ]
for A in array:
    ans = solu.maxset(A[0])
    print("output for ",A," is ",ans)
