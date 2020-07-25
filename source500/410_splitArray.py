from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        if not nums: return 0
        n = len(nums)
        dp = [[10**18]*(m+1) for _ in range(n+1)]
        sub = [0]
        for i in nums:
            sub.append(sub[-1]+i)
        dp[0][0] = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j-1], sub[i]-sub[k]))
        return dp[n][m]