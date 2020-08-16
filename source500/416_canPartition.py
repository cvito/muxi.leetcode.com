from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums: return False
        sum_nums = 0
        for i in nums: sum_nums += i
        if sum_nums & 1 == 1: return False

        #dp[i][j]: 前i个取其中几个，其值等于j
        target = int(sum_nums / 2)
        dp = [[0] * (target+1) for _ in nums]
        if nums[0] <= target:
            dp[0][nums[0]] = True

        for i in range(1, len(nums)):
            for j in range(target+1):
                dp[i][j] = dp[i-1][j]
                if nums[i] == j:
                    dp[i][j] = True
                    continue
                if nums[i] < j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        return dp[len(nums)-1][target]

s = Solution()
r = s.canPartition([1, 5, 11, 5])
print(r)