class Solution:
    # @param A : list of strings
    # @return a list of strings
    # def solveA(self, A):
    #     n = len(A)
    #     ans = []

    def solve(self, A):
        n = len(A)
        map = [[] * 1 for _ in range(100)]
        ans = []
        for i in range(n):
            str = A[i]
            m = len(str)
            mark = ''
            for j in range(m-1,m-4,-1):
                if ord(str[j]) < 58 and ord(str[j]) > 47:
                    mark += str[j]
                else:
                    break
            mark = mark[::-1]
            map[int(mark)-1].append(i)
        for i in range(99,-1,-1):
            for ele in map[i]:
                ans.append(A[ele])
        return ans



solu = Solution()
array = [
    [["adarsh80","harsh95","shivam95"]] , # ["harsh95","shivam95","adarsh80"]
    [["ravi1","m100"]] , # ["harsh95","shivam95","adarsh80"]
]
for A in array:
    ans = solu.solve(A[0])
    print("output for ",A," is ",ans)

# python3 intermediate/day_46/q3.py