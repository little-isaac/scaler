"""
Given a undirected graph and source node, destination node,
check if node(destination) can be visited from source node.

"""
from collections import deque

class Solution:
    def storeGraph(self, A):
        n = A[0][0]
        e = A[0][1]
        l = [None]*(n+1)
        for i in range(e):
            if l[A[1][i][0]] is None:
                l[A[1][i][0]] = [A[1][i][1]]
            else:
                l[A[1][i][0]].append(A[1][i][1])

            if l[A[1][i][1]] is None:
                l[A[1][i][1]] = [A[1][i][0]]
            else:
                l[A[1][i][1]].append(A[1][i][0])
        return l
    def solve(self, A, s, d):
        g = self.storeGraph(A)
        n = A[0][0]
        e = A[0][1]
        visited = [False] * (n+1)
        q = deque([])
        q.append(s)
        visited[s] = True
        while len(q) > 0:
            node = q.popleft()
            visit = g[node]
            if visit is None:
                continue
            for i in range(len(visit)):
                if visited[visit[i]] is not True:
                    visited[visit[i]] = True
                    q.append(visit[i])
        return visited[d]

if __name__ == "__main__":
    solu = Solution()
    array = [
        [
            [
                [6,7],
                [
                    [1,2],
                    [1,4],
                    [2,4],
                    [2,3],
                    [3,5],
                    [5,6],
                    [4,5]
                ]
             ],1,6
        ] ,
    ]
    for A in array:
        ans = solu.solve(A[0],A[1],A[2])
        print("output for ",A," is ",ans)
# solu = Solution()
# array = [
#     [] , 
# ]
# for A in array:
#     ans = solu.solve(A[0],A[1])
#     print("output for ",A," is ",ans)

