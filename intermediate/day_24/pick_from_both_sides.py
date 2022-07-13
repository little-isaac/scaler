"""
Problem Description
You are given an integer array A of size N.

You have to pick B elements in total. Some (possibly 0) elements from left end of array A and some (possibly 0) from the right end of array A to get the maximum sum.

Find and return this maximum possible sum.

NOTE: Suppose B = 4, and array A contains 10 elements, then

You can pick the first four elements or can pick the last four elements, or can pick 1 from front and 3 from the back, etc. You need to return the maximum possible sum of elements you can pick.


Problem Constraints
1 <= N <= 105

1 <= B <= N

-103 <= A[i] <= 103



Input Format
First argument is an integer array A.

Second argument is an integer B.



Output Format
Return an integer denoting the maximum possible sum of elements you picked.



Example Input
Input 1:

 A = [5, -2, 3 , 1, 2]
 B = 3
Input 2:

 A = [1, 2]
 B = 1


Example Output
Output 1:

 8
Output 2:

 2


Example Explanation
Explanation 1:

 Pick element 5 from front and element (1, 2) from back so we get 5 + 1 + 2 = 8
Explanation 2:

 Pick element 2 from end as this is the maximum we can get
"""
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def rangeSumLeft(self, l, r, pf):
        if l == 0:
            return pf[r]
        else:
            return pf[r] - pf[l-1]
    def rangeSumRight(self, l, r, pf):
        n = len(pf)
        if r == n-1:
            return pf[l]
        else:
            return pf[l] - pf[r-1]
    def firstApproach(self,A,B):
        n = len(A)
        ans = [0] * (B+1)
        left = [0] * n
        right = [0] * n
        left[0] = A[0]
        right[n-1] = A[n-1]
        for i in range(1,n):
            left[i] = left[i-1] + A[i]
        for j in range(n-2,-1,-1):
            right[j] = right[j+1] + A[j]
        for i in range(0,B+1):
            if i == 0:
                ans[i] = self.rangeSumLeft(0,B-1,left)
            elif i == B:
                ans[i] = self.rangeSumRight(n-i,n-1,right)
            else:
                ans[i] = self.rangeSumLeft(0,B-1-i,left) + self.rangeSumRight(n-i,n-1,right)
        maximum = ans[0]
        for ele in ans:
            if maximum < ele:
                maximum = ele
        return maximum

    def secondApproach(self,A,B):
        maximum = 0
        n = len(A)
        curr = 0
        for i in range(0,B):
            curr = curr + A[i]
        maximum = curr
        for i in range(0,B):
            # print(B-i,n-1-i)
            # continue
            curr = curr - A[B-1-i] + A[n-1-i]
            maximum = max(maximum,curr)
            # print(maximum,curr,"A["+str(B-1-i)+"]",A[B-1-i],"A["+str(n-1-i)+"]",A[n-1-i])
        return maximum
    def solve(self, A, B):
        # return self.firstApproach(A,B)
        return self.secondApproach(A,B)


solu = Solution()
array = [
    # [[5, -2, 3 , 1, 2],3], # 8
    # [[5, -2, 3 , 1, 2],4], # 11
    # [[1, 2],1], # 2
    # [[ -969, -948, 350, 150, -59, 724, 966, 430, 107, -809, -993, 337, 457, -713, 753, -617, -55, -91, -791, 758, -779, -412, -578, -54, 506, 30, -587, 168, -100, -409, -238, 655, 410, -641, 624, -463, 548, -517, 595, -959, 602, -650, -709, -164, 374, 20, -404, -979, 348, 199, 668, -516, -719, -266, -947, 999, -582, 938, -100, 788, -873, -533, 728, -107, -352, -517, 807, -579, -690, -383, -187, 514, -691, 616, -65, 451, -400, 249, -481, 556, -202, -697, -776, 8, 844, -391, -11, -298, 195, -515, 93, -657, -477, 587 ],81] #-5453
    [[ -584, -714, -895, -512, -718, -545, 734, -886, 701, 316, -329, 786, -737, -687, -645, 185, -947, -88, -192, 832, -55, -687, 756, -679, 558, 646, 982, -519, -856, 196, -778, 129, -839, 535, -550, 173, -534, -956, 659, -708, -561, 253, -976, -846, 510, -255, -351, 186, -687, -526, -978, -832, -982, -213, 905, 958, 391, -798, 625, -523, -586, 314, 824, 334, 874, -628, -841, 833, -930, 487, -703, 518, -823, 773, -730, 763, -332, 192, 985, 102, -520, 213, 627, -198, -901, -473, -375, 543, 924, 23, 972, 61, -819, 3, 432, 505, 593, -275, 31, -508, -858, 222, 286, 64, 900, 187, -640, -587, -26, -730, 170, -765, -167, 711, 760, -104, -333 ],32] # 727
]
for A in array:
    ans = solu.solve(A[0],A[1])
    print("output for ",A," is ",ans)