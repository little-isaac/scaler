"""
Problem Description
You are given a string A of size N.

Return the string A after reversing the string word by word.

NOTE:

A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.


Problem Constraints
1 <= N <= 3 * 105



Input Format
The only argument given is string A.



Output Format
Return the string A after reversing the string word by word.



Example Input
Input 1:
    A = "the sky is blue"
Input 2:
    A = "this is ib"


Example Output
Output 1:
    "blue is sky the"
Output 2:
    "ib is this"    


Example Explanation
Explanation 1:
    We reverse the string word by word so the string becomes "the sky is blue".
Explanation 2:
    We reverse the string word by word so the string becomes "this is ib".
"""
class Solution:
    # @param A : string
    # @return a strings
    def appOne(self, A):
        A = A.strip()
        A = A.split()
        A = A[::-1]
        return ' '.join(A)
    def appTwo(self, A):
        A = A.strip()
        listA = list(A)
        n = len(listA)
        listA = self.replaceArray(listA,0,n-1)
        s = 0
        e = -1
        for i in range(n):
            if listA[i] == ' ' or i == n-1:
                if i == n-1:
                    e = i
                else:
                    e = i-1
                listA = self.replaceArray(listA,s,e)
                s = i+1
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
        return self.appOne(A)


solu = Solution()
array = [
    ["the sky is blue"] , # the sky is blue
    ["this is ib"] , # this is ib
]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)