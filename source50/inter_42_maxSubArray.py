from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        if len(nums) == 1: return res
        for i in range(1, len(nums)):
            if nums[i-1] > 0: nums[i] += nums[i-1]
            if nums[i] > res: res = nums[i]
        return res