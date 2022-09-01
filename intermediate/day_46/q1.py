class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of strings
    # @return a strings
    def binToDeci(self,a):
        return int(a,2)

    def deciToBin(self,a):
        return bin(a).replace('0b','')

    def inverse(self,b):
        return b.replace('0','2').replace('1','0').replace('2','1')

    def solve(self, A, B, C):
        n = A
        ans = 0
        totalOp = 0
        rev = []

        for i in range(n):
            binEle = C[i]
            binREle = self.inverse(binEle)
            oEle = self.binToDeci(binEle)
            rEle = self.binToDeci(binREle)
            if rEle > oEle:
                rev.append(rEle)
            else:
                ans += oEle

        rev.sort(reverse=True)
        for i in range(len(rev)):
            binEle = self.deciToBin(rev[i])
            binREle = self.inverse(binEle)
            oEle = self.binToDeci(binEle)
            rEle = self.binToDeci(binREle)
            if totalOp < B:
                ans += oEle
                totalOp += 1
            else:
                ans += rEle
        return self.deciToBin(ans)
    def solveA(self, A, B, C):
        n = A
        ans = 0
        totalOp = 0
        for i in range(n):
            binEle = C[i]
            binREle = self.inverse(binEle)

            oEle = self.binToDeci(binEle)
            rEle = self.binToDeci(binREle)
            if oEle < rEle and totalOp < B:
                totalOp += 1
                ans += rEle
            else:
                ans += oEle
            print(ans,binEle,binREle,oEle,rEle)
        return self.deciToBin(ans)


solu = Solution()
array = [
    [2,1,["11","01"]] , # 101
    [3,2,["100","011","011"]] , #1100
    [3,2,["011","011","001"]], #1101
    [8,2,["1","1","0","0","1","1","1","1"]], #1101
]
for A in array:
    ans = solu.solve(A[0],A[1],A[2])
    print("output for ",A," is ",ans)

# python3 intermediate/day_46/q1.py