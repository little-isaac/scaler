class Solution:
    # @param A : string
    # @return a strings
    def appOne(self, A):
        A = A.strip()
        # A = A.split()
        A = A[::-1]
        return A
    def appTwo(self, A):
        A = A.strip()
        listA = list(A)
        n = len(listA)
        listA = self.replaceArray(listA,0,n-1)
        return "".join(listA)


    def replaceArray(self,arr,s,e):
        i = s
        j = e
        while(i<j):
            arr[i],arr[j] = arr[j],arr[i]
            i = i + 1
            j = j - 1
        return arr

    def solve(self, A):
        return self.appTwo(A)
        return self.appOne(A)


solu = Solution()
array = [
    ["scaler"] , # the sky is blue
    ["academy"] , # this is ib
]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)