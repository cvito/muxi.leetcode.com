from typing import List


# 超时
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        len_nums = len(nums)
        res_max = nums[-1]
        dp = [[0]*len_nums for _ in nums]
        for i in range(len_nums-1, -1, -1):
            for j in range(i, len_nums):
                if j == i:
                    dp[i][j] = nums[i]
                else:
                    dp[i][j] = nums[i] * dp[i+1][j]
                res_max = max(res_max, dp[i][j])
        return res_max

class Solution_V2:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        len_nums = len(nums)
        res = nums[0]
        dp = [[nums[0], nums[0]]] + [[0, 0] for _ in range(len_nums - 1)]
        for i in range(1, len_nums):
            max_res = dp[i-1][0] * nums[i] if nums[i] > 0 else dp[i-1][1] * nums[i]
            dp[i][0] = max(max_res, nums[i])
            min_res = dp[i-1][1] * nums[i] if nums[i] > 0 else dp[i-1][0] * nums[i]
            dp[i][1] = min(min_res, nums[i])
            res = max(res, dp[i][0])
        return res

class Solution_V3:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [[0, 0] for _ in range(2)]
        dp[0][0], dp[0][1], res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            x, y = i % 2, (i-1) % 2
            dp[x][0] = max(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            dp[x][1] = min(dp[y][1] * nums[i], dp[y][0] * nums[i], nums[i])
            res = max(res, dp[x][0])
        return res

s = Solution_V2()
r = s.maxProduct([-2])
print(r)