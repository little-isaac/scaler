class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        ans = 1
        n = len(A)
        A = list(A)
        freq = {}
        for i in range(n):
            ele = A[i]
            if freq.get(ele):
                freq[ele] += 1
            else:
                freq[ele] = 1
        if n & 1 == 0:
            for i in freq:
                count = freq.get(i)
                if count & 1 == 1:
                    ans = 0
                    break
        else:
            isOneFound = False
            for i in freq:
                count = freq.get(i)
                if count & 1 == 1:
                    if isOneFound is False:
                        isOneFound = True
                    else:
                        ans = 0
                        break
        return ans
solu = Solution()
array = [
    ["aabb"] , # 1
    ["aecbb"] , # 0
    ["aacbb"] , # 1
    ["hddavxfqmfvgwicsgbunqokernzxslxuyffflngrhw"] , # 1
]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)

# python3 intermediate/day_46/q4.py