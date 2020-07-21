from functools import lru_cache
from typing import List


# 超时
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums: return 0
        val = [1] + nums + [1]

        @lru_cache
        def heler(left, right) -> int:
            if left >= right-1: return 0
            rsp = 0
            for i in range(left+1, right):
                total = val[left]*val[i]*val[right]
                total += heler(left, i) + heler(i, right)
                rsp = max(rsp, total)
            return rsp
        return heler(0, len(nums)+1)

class Solution_V2:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dp = [[0] * (n+2) for _ in range(n+2)]
        val = [1] + nums + [1]
        for i in range(n-1, -1, -1):
            for j in range(i+2, n+2):
                for k in range(i+1, j):
                    total = val[i] * val[k] * val[j]
                    total += dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], total)
        return dp[0][n+1]
                           


s = Solution()
r = s.maxCoins([3,1,5,8])
print(r)