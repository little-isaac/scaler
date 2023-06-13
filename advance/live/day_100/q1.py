"""


"""
import heapq

class Solution:
    def solve1(self, A, K):
        heap = []
        n = len(A)
        ans = []
        for i in range(n):
            heapq.heappush(heap, A[i])
        for i in range(K):
            ans.append(heapq.heappop(heap))
        return ans
    def solve(self, A, K):
        heap = []
        n = len(A)
        ans = []
        for i in range(K):
            heapq.heappush(heap, -1 * A[i])
        for i in range(K,n):
            max = -1 * heap[0]
            if A[i] < max:
                heapq.heappop(heap)
                heapq.heappush(heap, -1 * A[i])
        for i in range(K):
            ans.append(heapq.heappop(heap) * -1)
        return ans[::-1]

if __name__ == "__main__":
    solu = Solution()
    array = [
        [[8, 3, 10, 4, 11, 2, 7, 6, 5, 1] ,4],
        [[-3, 6, 2, 0, 8, 7, 10, 4] ,3]
    ]
    for A in array:
        ans = solu.solve(A[0], A[1])
        print("output for ",A," is ",ans)