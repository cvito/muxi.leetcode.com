import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix: return 0
        hp = [(matrix[i][0], i, 0) for i in range(len(matrix))]
        heapq.heapify(hp)
        for i in range(k-1):
            min_num, x, y = heapq.heappop(hp)
            if y < len(matrix[x])-1:
                heapq.heappush(hp, (matrix[x][y+1], x, y+1))
        return heapq.heappop(hp)[0]

s = Solution()
rsp = s.kthSmallest([
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
], 8)
print(rsp)