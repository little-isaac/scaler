"""
Problem Description
You are given an array A consisting of heights of Christmas trees and an array B of the same size consisting of the cost of each of the trees (Bi is the cost of tree Ai, where 1 ≤ i ≤ size(A)), and you are supposed to choose 3 trees (let's say, indices p, q, and r), such that Ap < Aq < Ar, where p < q < r.
The cost of these trees is Bp + Bq + Br.

You are to choose 3 trees such that their total cost is minimum. Return that cost.

If it is not possible to choose 3 such trees return -1.



Problem Constraints
1 <= A[i], B[i] <= 109
3 <= size(A) = size(B) <= 3000



Input Format
First argument is an integer array A.
Second argument is an integer array B.



Output Format
Return an integer denoting the minimum cost of choosing 3 trees whose heights are strictly in increasing order, if not possible, -1.



Example Input
Input 1:

 A = [1, 3, 5]
 B = [1, 2, 3]
Input 2:

 A = [1, 6, 4, 2, 6, 9]
 B = [2, 5, 7, 3, 2, 7]


Example Output
Output 1:

 6 
Output 2:

 7 


Example Explanation
Explanation 1:

 We can choose the trees with indices 1, 2 and 3, and the cost is 1 + 2 + 3 = 6. 
Explanation 2:

 We can choose the trees with indices 1, 4 and 5, and the cost is 2 + 3 + 2 = 7. 
 This is the minimum cost that we can get.
"""


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        ans = float('inf')
        for i in range(1,n-1):
            centerB = B[i]
            centerA = A[i]
            centerI = i

            leftI = None
            leftA = None
            leftB = None
            j = i-1
            while j > -1:
                if A[j] < centerA:
                    if leftB is None or B[j] < leftB:
                        leftA = A[j]
                        leftB = B[j]
                        leftI = j
                j -= 1
            if leftI is None:
                continue

            rightI = None
            rightA = None
            rightB = None
            j = i+1
            while j < n:
                if A[j] > centerA:
                    if rightB is None or B[j] < rightB:
                        rightA = A[j]
                        rightB = B[j]
                        rightI = j
                j += 1
            if rightI is None:
                continue
            sum = leftB + centerB + rightB
            ans = min(ans,sum)

        if ans == float('inf'):
            return -1
        return ans


solu = Solution()
array = [
    # [[1, 3, 5],[1, 2, 3]] , # 6

    # 0  1  2  3  4  5   0  1  2  3  4  5
    [[1, 6, 4, 2, 6, 9],[2, 5, 7, 3, 2, 7]] ,  # 7

    # 0  1  2  3  4  5   0  1  2  3  4  5
    [[3, 2, 1, 2, 3, 4],[1, 2, 3, 4, 5, 6]] ,  # 12
]
for A in array:
    ans = solu.solve(A[0],A[1])
    print("output for ",A," is ",ans)