from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices: return 0
        if k >= len(prices)//2:
            return self.maxProfit_inf(prices)

        dp = [[[0 for _ in range(2)] for _ in range(k+1)] for _ in range(len(prices))]
        for i in range(k+1):
            dp[0][i][0], dp[0][i][1] = 0, -prices[0]

        for i in range(1, len(prices)):
            for j in range(k+1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][1]+prices[i]) if j != 0 else dp[i-1][j][0]
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j][0]-prices[i])

        res = 0
        for i in range(k + 1):
            res = max(res, dp[len(prices) - 1][i][0])
        return res

    def maxProfit_inf(self, prices: List[int]) -> int:
        if not prices: return 0
        dp = [[0]*2 for _ in range(len(prices))]
        dp[0][0], dp[0][1] = 0, -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[len(prices)-1][0]

s = Solution()
r = s.maxProfit(2,[3,2,6,5,0,3])  #7
# r = s.maxProfit(2,[2,4,1])  #2
print(r)