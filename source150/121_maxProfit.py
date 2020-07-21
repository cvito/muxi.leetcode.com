from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        res = 0
        dp = [[0 for _ in range(3)] for _ in range(len(prices))]
        #dp定义为到i天结束时，股票的最大收益
        #0-没有股票；1-拥有股票；2-卖出股票
        dp[0][0], dp[0][1], dp[0][2] = 0, -prices[0], 0
        for i in range(1, len(prices)):
            dp[i][0] = dp[i-1][0]
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
            res = max(res, dp[i][0], dp[i][1], dp[i][2])
        return res

s = Solution()
r = s.maxProfit([7,1,5,3,6,4])
print(r)