from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        def helper(i, j) -> int:
            if i >= len(grid) or j >= len(grid[0]): return 0
            if i == len(grid)-1 and j == len(grid[0])-1: return grid[i][j]
            r = helper(i, j+1)
            d = helper(i+1, j)
            if r == 0: return grid[i][j] + d
            if d == 0: return grid[i][j] + r
            print("i:{}, j:{}, r:{}, d:{}, result:{}".format(i, j, r, d, grid[i][j] + min(r, d)))
            return grid[i][j] + min(r, d)
        return helper(0, 0)

class Solution_V2:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        dp = [[0]*len(grid[0]) for _ in grid]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                    continue
                if j-1 < 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                    continue
                if i-1 < 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                    continue
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[len(grid)-1][len(grid[0])-1]


s = Solution_V2()
rsp = s.minPathSum([
  [1,3,1]
])
print(rsp)