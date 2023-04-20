"""
Quick sort - Divide and conquer

"""
class Solution:
    def partition(self,A,s,e):
        pivot = A[e]
        i = s - 1
        j = s
        while j <= e - 1:
            if A[j] < pivot:
                i = i + 1
                A[i],A[j] = A[j],A[i]
            j = j + 1
        A[i+1],A[e] = A[e],A[i+1]
        return i+1


    def quickSort(self,A,S,E):
        if S >= E:
            return
        p = self.partition(A,S,E)
        self.quickSort(A,S,p-1)
        self.quickSort(A,p+1,E)

    def solve(self, A):
        self.quickSort(A,0,len(A)-1)
        return A


# solu = Solution()
# array = [
#     [] , 
# ]
# for A in array:
#     ans = solu.solve(A[0],A[1])
#     print("output for ",A," is ",ans)

