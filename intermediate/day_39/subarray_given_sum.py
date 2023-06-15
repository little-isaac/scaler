class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        start = 0
        end = 0
        currSum = A[0]
        
        while end < len(A):
            if currSum == B:
                return A[start:end+1]
            elif currSum < B:
                end += 1
                if end < len(A):
                    currSum += A[end]
            else:
                currSum -= A[start]
                start += 1
        
        return [-1]

if __name__ == "__main__":
    #  A = [2, 7, 11, 15]
    #  B = 9
    #  A = [4,7,-4,2,2,2,3,-5,-3,9,-4,9,-7,7,-1,9,9,4,1,-4,-2,3,-3,-5,4,-7,7,9,-4,4,-8]
    #  B = -3
     A = [1, 2, 3, 4, 5]
     B = 5
    #  A = [5, 10, 20, 100, 105]
    #  B = 110
    #  A = [1, 100000]
    #  B = 100000
     sol = Solution()
     ans = sol.solve(A,B)
     print(ans)