from functools import lru_cache
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        dire_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        @lru_cache(None)
        def dfs(row: int, col: int) -> int:
            max_res = 1
            for dx, dy in dire_list:
                new_row, new_col = row+dx, col+dy
                if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] > matrix[row][col]:
                    max_res = max(max_res, dfs(new_row, new_col)+1)
            return max_res

        res = 1
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i, j))
        return res


class Solution_V2:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        n = len(matrix[0])
        m = len(matrix)
        #0-向上，1-向下，2-向左，3-向右, 4-最大
        dp = [[[0]*5 for _ in range(n+1)] for _ in range(m+1)]

        #左上
        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[i][j][0] = 1
                if j == 0:
                    dp[i][j][2] = 1
                if i != 0 and matrix[i][j] < matrix[i-1][j]:
                    dp[i][j][0] = 1 + dp[i-1][j][0]
                    dp[i][j][4] = max(dp[i][j][0], dp[i][j][4])
                if j != 0 and matrix[i][j] < matrix[i][j-1]:
                    dp[i][j][2] = 1 + dp[i][j-1][2]
                    dp[i][j][4] = max(dp[i][j][2], dp[i][j][4])
        #右下
        res = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1:
                    dp[i][j][1] = 1
                if j == n-1:
                    dp[i][j][3] = 1
                if i != m-1 and matrix[i][j] < matrix[i+1][j]:
                    dp[i][j][1] = 1 + dp[i+1][j][1]
                    dp[i][j][4] = max(dp[i][j][1], dp[i][j][4])
                if j != n-1 and matrix[i][j] < matrix[i][j+1]:
                    dp[i][j][3] = 1 + dp[i][j+1][3]
                    dp[i][j][4] = max(dp[i][j][3], dp[i][j][4])
                dp[i][j][4] = max(dp[i-1][j][4], dp[i+1][j][4], dp[i][j-1][4], dp[i][j+1][4])
                res = max(res, dp[i][j][4])
        return res

s = Solution()
r = s.longestIncreasingPath([
  [9,9,4,3],
  [6,6,8,2],
  [2,1,1,1]
] )
print(r)
