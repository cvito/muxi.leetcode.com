from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid: return 0
        len_row = len(obstacleGrid[0])
        len_col = len(obstacleGrid)
        if len_row == 0: return 1
        dp = [[0]*len_row for _ in range(len_col)]
        dp[len_col-1][len_row-1] = 0 if obstacleGrid[len_col-1][len_row-1] else 1
        for i in range(len_col-1, -1, -1):
            for j in range(len_row-1, -1, -1):
                if obstacleGrid[i][j] == 1: continue
                if j+1 < len_row:
                    dp[i][j] += dp[i][j+1]
                if i+1 < len_col:
                    dp[i][j] += dp[i+1][j]
        return dp[0][0]

s = Solution()
r = s.uniquePathsWithObstacles([[1]])
print(r)