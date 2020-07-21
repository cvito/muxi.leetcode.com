from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(len(prices))]
        dp[0][0][0], dp[0][0][1] = 0, -prices[0]
        dp[0][1][0], dp[0][1][1] = -float('inf'), -float('inf')
        dp[0][2][0], dp[0][2][1] = -float('inf'), -float('inf')

        for i in range(1, len(prices)):
            dp[i][0][0] = dp[i-1][0][0]
            dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][0][0]-prices[i])

            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][1]+prices[i])
            dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0]-prices[i])

            dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][1][1]+prices[i])
            dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0]-prices[i])
        end = len(prices)-1
        return max(dp[end][0][0], dp[end][1][0], dp[end][2][0])

s = Solution()
r = s.maxProfit([3,3,5,0,0,3,1,4])
print(r)