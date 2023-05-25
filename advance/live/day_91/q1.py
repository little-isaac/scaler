"""
Intro to deque

"""
class Solution:
    data = []
    def __init__(self) -> None:
        self.data = []
    def pushleft(self,x):
        self.data.insert(0, x)
    def popleft(self):
        if len(self.data) == 0:
            return None
        return self.data.pop(0)
    def append(self,x):
        self.data.append(x)
    def pop(self):
        if len(self.data) == 0:
            return None
        return self.data.pop(len(self.data)-1)
    def front(self):
        if len(self.data) == 0:
            return None
        return self.data[0]
    def rear(self):
        if len(self.data) == 0:
            return None
        return self.data[-1]

if __name__ == "__main__":
    solu = Solution()
    array = [
        [] ,
    ]
    for A in array:
        ans = solu.solve(A[0],A[1])
        print("output for ",A," is ",ans)

