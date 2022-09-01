class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        n = len(C)
        pf = [0]*n
        pf[0] = C[0]
        for i in range(1,n):
            if pf[i-1] == B:
                pf[i] = C[i]
            else:
                pf[i] = pf[i-1] + C[i]
        ans = float('inf')
        prev = pf[0]
        for i in range(1,n):
            if pf[i] == B:
                if prev == pf[i]:
                    ans = min(ans,1)
                    continue
                else:
                    continue
            else:
                eleToCheck = pf[i]
                c = 1
                for k in range(i+1,n):
                    if pf[k] == B:
                        continue
                    elif pf[k] == eleToCheck:
                        c += 1
                ans = min(ans,A-c)
        return ans


solu = Solution()
array = [
    [2,7,[3,4,2,2,3]] , # 1
    [3,5,[1,2,2,5,3,2]] , # 1
    [3,6,[1,2,3,3,3,3,3]] , # 0
    [4,6,[3,3,6,2,2,2,2,4]] , # 2
]
for A in array:
    ans = solu.solve(A[0],A[1],A[2])
    print("output for ",A," is ",ans)

# python3 intermediate/day_46/q5.py