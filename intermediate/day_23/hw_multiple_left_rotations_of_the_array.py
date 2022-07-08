"""
Problem Description
Given an array of integers A and multiple values in B, which represents the number of times array A needs to be left rotated.

Find the rotated array for each value and return the result in the from of a matrix where ith row represents the rotated array for the ith value in B.



Problem Constraints
1 <= length of both arrays <= 2000 -10^9 <= A[i] <= 10^9 0 <= B[i] <= 2000


Input Format
The first argument given is the integer array A.
The second argument given is the integer array B.


Output Format
Return the resultant matrix.


Example Input
Input 1:
 
    A = [1, 2, 3, 4, 5]
    B = [2, 3]

Input 2:

  
    A = [5, 17, 100, 11]
    B = [1]




Example Output
Output 1:
 
    [ [3, 4, 5, 1, 2]
     [4, 5, 1, 2, 3] ]


Output 2:

    
    [ [17, 100, 11, 5] ]



Example Explanation
for input 1 -> B[0] = 2 which requires 2 times left rotations

1: [2, 3, 4, 5, 1]

2: [3, 4, 5, 1, 2]

B[1] = 3 which requires 3 times left rotation

1: [2, 3, 4, 5, 1]

2: [3, 4, 5, 1, 2]

2: [4, 5, 1, 2, 4]

"""
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def replaceArray(self,arr,s,e):
        i = s
        j = e
        while(i<j):
            arr[i],arr[j] = arr[j],arr[i]
            i = i + 1
            j = j - 1
        return arr

    def leftRotation(self,arr,b):
        l = len(arr)

        b = b % l
        b = l - b
        arr = self.replaceArray(arr,0,l-1)
        arr = self.replaceArray(arr,0,b-1)
        arr = self.replaceArray(arr,b,l-1)

        return arr

    def solve(self, A, B):
        output = []
        for index,ele in enumerate(B):
            output.append(self.leftRotation(A[:],ele))
        return output


solu = Solution()
array = [
    [[1, 2, 3, 4, 5],[2,3]],
    [[5, 17, 100, 11],[1]]
]
for A in array:
    ans = solu.solve(A[0],A[1])
    print("output for ",A," is ",ans)