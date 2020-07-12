from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle: return 0
        m = len(triangle)
        dp = triangle[-1]
        for i in range(m-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]

s = Solution()
r = s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
print(r)
