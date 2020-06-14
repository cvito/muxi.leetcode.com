class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0: return 0
        way_sum = {1: k, 2: k * k}
        if n < 3:
            return way_sum[n]
        for i in range(3, n + 1):
            print(way_sum)
            way_sum[i] = (k - 1) * (way_sum[i - 1] + way_sum[i - 2])
        return way_sum[n]

s = Solution()
print(s.numWays(0, 0))