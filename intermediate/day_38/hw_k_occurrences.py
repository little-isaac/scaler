class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def getSum(self, N, B, A):
        hashA = {}
        for i in range(N):
            if A[i] in hashA:
                hashA[A[i]] += 1
            else:
                hashA[A[i]] = 1
        sum = 0
        isFound = False
        for ele in hashA:
            if hashA[ele] == B:
                isFound = True
                sum = sum + ele
        if isFound:
            return sum
        return -1


solu = Solution()
array = [
    [5,2,[1,2,2,3,3]] , # 5
]
for A in array:
    ans = solu.getSum(A[0],A[1],A[2])
    print("output for ",A," is ",ans)