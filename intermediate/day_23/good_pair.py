"""
Problem Description
Given an array A and an integer B. A pair(i, j) in the array is a good pair if i != j and (A[i] + A[j] == B). Check if any good pair exist or not.
"""

"""
Problem Constraints
1 <= A.size() <= 104

1 <= A[i] <= 109

1 <= B <= 109
"""

"""
Input Format
First argument is an integer array A.

Second argument is an integer B.

"""

"""
Output Format
Return 1 if good pair exist otherwise return 0.
"""

"""
Example Input
Input 1:

A = [1,2,3,4]
B = 7

Output 1:

1


Input 2:

A = [1,2,4]
B = 4

Output 2:

0


Input 3:

A = [1,2,2]
B = 4

Output 3:

1

"""

"""
Example Explanation
Explanation 1:

 (i,j) = (3,4)
Explanation 2:

No pair has sum equal to 4.
Explanation 3:

 (i,j) = (2,3)
 """

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def upper(self,A,B):
        n = len(A)
        i = 0
        j = 0
        for i in range(0,n-1):
            for j in range(i+1,n):
                if A[i] + A[j] == B:
                    return 1
                # print("("+str(i)+","+str(j)+")")

        return 0

    def lower(self,A,B):
        n = len(A)
        i = 0
        j = 0
        for i in range(1,n):
            for j in range(0,i):
                if A[i] + A[j] == B:
                    return 1
                # print("("+str(i)+","+str(j)+")")

        return 0

    def solve(self, A, B):
        # return self.upper(A,B)
        return self.lower(A,B)


solu = Solution()
array = [
        [
            [1,2,3,4],
            7
        ],
        [
            [1,2,4],
            4
        ],
        [
            [1,2,2],
            4
        ]
    ]
for A in array:
    ans = solu.solve(A[0],A[1])
    print("output for ",A," is ",ans)
