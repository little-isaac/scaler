"""
Given arr[n] elements sort the array

"""
import os
import sys
sys.path.append(os.getcwd())
# sys.setrecursionlimit(100 * 100)

from advance.live.day_69.q5 import Solution as merge

class Solution:
    def mergeSort(self,A,s,e):
        if s >= e:
            return
        m = (s+e) // 2
        self.mergeSort(A,s,m)
        self.mergeSort(A,m+1,e)
        mergeClass = merge()
        mergeClass.solve(A,s,m,e)
    def solve(self,A):
        self.mergeSort(A,0,len(A)-1)
        return A

# solu = Solution()
# array = [
#     [] , 
# ]
# for A in array:
#     ans = solu.solve(A[0],A[1])
#     print("output for ",A," is ",ans)

