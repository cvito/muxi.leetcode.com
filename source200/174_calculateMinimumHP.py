from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon: return 0
        dp = [[0]*len(dungeon[0]) for _ in dungeon]
        n = len(dungeon[0])
        m = len(dungeon)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    dp[i][j] = 1
                    continue
                if i == m-1 and j < n:
                    dp[i][j] = max(dp[i][j+1] - dungeon[i][j+1], 0)
                    continue
                if j == n-1 and i < m:
                    dp[i][j] = max(dp[i+1][j] - dungeon[i+1][j], 0)
                    continue
                right = max(dp[i][j+1] - dungeon[i][j+1], 0)
                down = max(dp[i+1][j] - dungeon[i+1][j], 0)
                dp[i][j] = min(right, down)
        return max(dp[0][0]-dungeon[0][0], 0)

s = Solution()
r = s.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]])
print(r)


