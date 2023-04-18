"""
Given arr[n], calculate number of pairs [i,j]
such that i < j and a[i] > a[j]

"""
class Solution:
    count = 0
    def mergeSort(self,A,i,j):
        if i >= j:
            return A
        m = (i+j) // 2
        A = self.mergeSort(A,i,m)
        A = self.mergeSort(A,m+1,j)
        return self.merge(A,i,m,j)
    def merge(self,A, s1, e1, e2):
        n1 = e1+1
        n2 = e2+1
        p1 = s1
        p2 = e1+1
        C = []
        for i in range(p1):
            C.append(A[i])
        while p1 < n1 and p2 < n2:
            if A[p1] < A[p2]:
                C.append(A[p1])
                p1 = p1 + 1
            else:
                self.count = self.count + (n1 - p1)
                C.append(A[p2])
                p2 = p2 + 1
        while p1 < n1:
            C.append(A[p1])
            p1 = p1 + 1
        while p2 < n2:
            C.append(A[p2])
            p2 = p2 + 1
        for i in range(e2+1,len(A),1):
            C.append(A[i])
        return C
    def solve(self,A):
        sortedA = self.mergeSort(A,0,len(A)-1)
        return self.count

# solu = Solution()
# array = [
#     [] , 
# ]
# for A in array:
#     ans = solu.solve(A[0],A[1])
#     print("output for ",A," is ",ans)

