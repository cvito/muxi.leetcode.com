from typing import List


class Solution:
    #动态规划思路:前一个节点的val为有效值才附加进来新节点上
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > 0: nums[i] += nums[i-1]
        return max(nums)

    #贪心算法思路：
    def maxSubArrayV2(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        cur_sum_max = sum_max = nums[0]
        for i in range(1, len(nums)):
            if cur_sum_max < 0: cur_sum_max = nums[i]
            else: cur_sum_max += nums[i]
            sum_max = max(sum_max, cur_sum_max)
        return sum_max