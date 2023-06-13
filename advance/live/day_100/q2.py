"""
Median : A point which divides data into 2 halves.

Given an array, median of all prefix subarrays [ running median]
"""
import heapq

class Solution:
    def solve(self, A):
        leftHeap = []
        rightHeap = []
        n = len(A)
        ans = []
        heapq.heappush(leftHeap, -1 * A[0])
        ans.append(A[0])
        for i in range(1, n):
            if A[i] < -1 * leftHeap[0]:
                heapq.heappush(leftHeap, -1 * A[i])
            else:
                heapq.heappush(rightHeap, A[i])

            if len(leftHeap) < len(rightHeap):
                ele = heapq.heappop(rightHeap)
                heapq.heappush(leftHeap, -1 * ele)
            elif len(leftHeap) - len(rightHeap) > 1:
                ele = -1 * heapq.heappop(leftHeap)
                heapq.heappush(rightHeap, ele)
            
            l = i + 1
            if l % 2 == 0:
                min = rightHeap[0]
                max = -1 * leftHeap[0]
                ans.append((max + min) // 2)
            else:
                ans.append(-1 * leftHeap[0])

        return leftHeap, rightHeap, ans
if __name__ == "__main__":
    solu = Solution()
    array = [
        [9, 6, 3, 10, 4],
    ]
    for A in array:
        ans = solu.solve(A)
        print("output for ",A," is ",ans)


        