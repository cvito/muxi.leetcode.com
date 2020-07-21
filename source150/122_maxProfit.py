from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        dp = [[0]*2 for _ in range(len(prices))]
        dp[0][0], dp[0][1] = 0, -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[len(prices)-1][0]

s = Solution()
r = s.maxProfit([3,2,6,5,0,3])
print(r)