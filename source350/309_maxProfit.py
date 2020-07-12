import heapq
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        dp = [[-prices[0], 0, 0]] + [[int]*3 for _ in range(n-1)]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2]-prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][2], dp[i-1][1])
        return max(dp[n-1][1], dp[n-1][2])

s = Solution()
r = s.maxProfit([1,2,3,0,2])
print(r)