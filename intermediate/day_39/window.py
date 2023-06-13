class Solution:
     # @param A : list of integers
     # @param B : integer
     # @return a list of integers
     def dNums(self, A, B):
        n = len(A)
        hashMap = {}
        ans = [0]*(n-B+1)
        for i in range(B):
            if A[i] in hashMap:
                hashMap[A[i]] = hashMap[A[i]] + 1
            else:
                hashMap[A[i]] = 1
                ans[0] = ans[0] + 1
        i = 0
        j = i + B
        counter = 1
        while j < n:
            remove = A[i]
            add = A[j]
            oldCount = ans[counter-1]
            hashMap[remove] = hashMap[remove] - 1
            if hashMap[remove] == 0:
                oldCount = oldCount - 1
                del hashMap[remove]
            if add in hashMap:
                hashMap[add] = hashMap[add] + 1
            else:
                hashMap[add] = 1
                oldCount = oldCount + 1
            ans[counter] = oldCount
            i = i + 1
            j = j + 1
            counter = counter + 1
        return ans

if __name__ == "__main__":
    A = [1,2,1,3,4,3]
    B = 3
    A = [1,1,2,2]
    B = 1
#  expected 0
    sol = Solution()
    ans = sol.dNums(A,B)
    print(ans)