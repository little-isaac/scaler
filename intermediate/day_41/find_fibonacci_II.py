class Solution:
    # @param A : integer
    # @return an integer
    def findAthFibonacci(self, A):
        if A <= 1:
            return A
        return self.findAthFibonacci(A-1) + self.findAthFibonacci(A-2)


solu = Solution()
array = [
    [2] , # 1
    [1] , # 1
    [0] , # 0
    [9] , # 34
]
for A in array:
    ans = solu.findAthFibonacci(A[0])
    print("output for ",A," is ",ans)