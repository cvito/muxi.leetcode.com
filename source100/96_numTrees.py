class Solution:
    def numTrees(self, n: int) -> int:
        if n < 3: return n
        dp = [0]*(n+1)
        dp[0], dp[1], dp[2] = 1, 1, 2
        for i in range(3, n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-1-j]
        return dp[n]

s = Solution()
r = s.numTrees(5)
print(r)


