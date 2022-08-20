"""
Problem Description
Eight integers A, B, C, D, E, F, G, and H represent two rectangles in a 2D plane.
For the first rectangle, its bottom left corner is (A, B), and the top right corner is (C, D), and for the second rectangle, its bottom left corner is (E, F), and the top right corner is (G, H).

Find and return whether the two rectangles overlap or not.



Problem Constraints
-10000 <= A < C <= 10000

-10000 <= B < D <= 10000

-10000 <= E < G <= 10000

-10000 <= F < H <= 10000



Input Format
The eight arguments are integers A, B, C, D, E, F, G, and H.


Output Format
Return 1 if the two rectangles overlap else, return 0.


Example Input
Input 1:

A = 0   B = 0
C = 4   D = 4
E = 2   F = 2
G = 6   H = 6
 
Input 2:

A = 0   B = 0
C = 4   D = 4
E = 2   F = 2
G = 3   H = 3


Example Output
Output 1:
1
Output 2:

1


Example Explanation
Explanation 1:
Rectangle with bottom left (2, 2) and top right (4, 4) is overlapping.
Explanation 2:

Overlapping rectangles can be found.
"""

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @param F : integer
    # @param G : integer
    # @param H : integer
    # @return an integer
    def solve(self, A, B, C, D, E, F, G, H):
        if C <= E or D <= F or A >= G or B >= H:
            return 0
        return 1

solu = Solution()
array = [
    [[0,0],[4,4],[2,2],[6,6]] , # 1
    [[0,0],[4,4],[2,2],[3,3]] , # 1
]
for A in array:
    ans = solu.solve(A[0][0],A[0][1],A[1][0],A[1][1],A[2][0],A[2][1],A[3][0],A[3][1])
    print("output for ",A," is ",ans)