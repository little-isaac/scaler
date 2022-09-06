class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        current = 1
        ans = []
        count = 0
        while count < A:
            current = current * 5
            n = len(ans)
            ans.append(current)
            count += 1
            for j in range(n):
                ans.append(current + ans[j])
                count += 1
        return ans[A-1]

solu = Solution()
array = [
    [1] , # 5     1
    [2] , # 25    2
    [3] , # 30
    [4] , # 125   3
    [5] , # 130
    [6] , # 150
    [7] , # 155
    [8] , # 625   4
    [9] , # 630
    [10] , # 650
    [73]
]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)