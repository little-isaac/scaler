"""
Given arr[n], calculate number of pairs [i,j]
such that i < j and a[i] > a[j]

"""
class Solution:
    count = 0
    def mergeSort(self,A,i,j):
        if i >= j:
            return
        m = (i+j) // 2
        self.mergeSort(A,i,m)
        self.mergeSort(A,m+1,j)
        self.merge(A,i,m,j)
    def merge(self,A, s1, e1, e2):
        n = e1+1
        m = e2+1
        p1 = s1
        p2 = e1+1
        C = [0] * (e2-s1+1)
        k = 0

        while p1 < n and p2 < m:
            if A[p1] < A[p2]:
                C[k] = A[p1]
                p1 = p1 + 1
                k = k + 1
            else:
                print(A[p1],A[p2])
                self.count = self.count + (n-p1)
                C[k] = A[p2]
                p2 = p2 + 1
                k = k + 1
        while p1 < n:
            C[k] = A[p1]
            p1 = p1 + 1
            k = k + 1
        while p2 < m:
            C[k] = A[p2]
            p2 = p2 + 1
            k = k + 1
        for i in range(len(C)):
            A[i+s1] = C[i]
    def solve(self,A):
        sortedA = self.mergeSort(A,0,len(A)-1)
        print(A)
        return self.count

# solu = Solution()
# array = [
#     [] , 
# ]
# for A in array:
#     ans = solu.solve(A[0],A[1])
#     print("output for ",A," is ",ans)

