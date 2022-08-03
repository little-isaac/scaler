"""
Problem Description
Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order and return the generated square matrix.



Problem Constraints
1 <= A <= 1000



Input Format
First and only argument is integer A


Output Format
Return a 2-D matrix which consists of the elements added in spiral order.



Example Input
Input 1:

1
Input 2:

2
Input 3:

5


Example Output
Output 1:

[ [1] ]
Output 2:

[ [1, 2], [4, 3] ]
Output 2:

[ [1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9] ]


Example Explanation
Explanation 1:

Only 1 is to be arranged.
Explanation 2:

1 --> 2
      |
      |
4<--- 3
Explanation 3:

image - https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/007/629/original/SS.png?1658222084
"""

class Solution:
	# @param A : integer
	# @return a list of list of integers
    def generateMatrix(self, A):
        totalElement = A * A
        move = 'tltr'
        ans = [[0] * A for _ in range(A)]
        i = 0
        j = 0
        r = 0
        for s in range(0,totalElement):
            ans[i][j] = s+1
            if move == 'tltr':  # top left to right
                if j == A-r-1:
                    move = 'rttb'
                    i += 1
                else:
                    j += 1
            elif move == 'rttb': # right top to bottom
                if i == A-r-1:
                    move = 'brtl'
                    j -= 1
                else:
                    i += 1
            elif move == 'brtl': # bottom right to left
                if j == r:
                    move = 'lbtt'
                    i -= 1
                else:
                    j -= 1
            elif move == 'lbtt': # left bottom to top
                if i == r + 1:
                    move = 'tltr'
                    r += 1
                    j += 1
                else:
                    i -= 1

        return ans





solu = Solution()
array = [
    [1] , # [ [1] ]
    [2] , # [ [1, 2], [4, 3] ]
    [5] , # [ [1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9] ]
]
for A in array:
    ans = solu.generateMatrix(A[0])
    print("output for ",A," is ",ans)