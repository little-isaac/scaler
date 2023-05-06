"""
Permutations of A in B
Count no of substrings of B which are permutation of A
"""
class Solution:
    def solve(self,A,B):
        n = len(B)
        m = len(A)
        i = 0
        j = m - 1
        hashMap = {}
        compareHashMap = {}
        for k in range(m):
            if A[k] in compareHashMap:
                compareHashMap[A[k]] = compareHashMap[A[k]] + 1
            else:
                compareHashMap[A[k]] = 1
            if B[k] in hashMap:
                hashMap[B[k]] = hashMap[B[k]] + 1
            else:
                hashMap[B[k]] = 1
        ans = 0  # Move initialization of ans here
        while j < n:
            if hashMap == compareHashMap:
                ans = ans + 1
            hashMap[B[i]] = hashMap[B[i]] - 1
            if hashMap[B[i]] == 0:
                del hashMap[B[i]]
            i = i + 1
            j = j + 1
            if j < n:  # Add this condition to avoid index out of range error
                if B[j] in hashMap:
                    hashMap[B[j]] =  hashMap[B[j]] + 1
                else:
                    hashMap[B[j]] = 1
        return ans

# solu = Solution()
# array = [
#     [] , 
# ]
# for A in array:
#     ans = solu.solve(A[0],A[1])
#     print("output for ",A," is ",ans)

