from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major_index = 0
        core_sum = 0
        for i, val in enumerate(nums):
            if core_sum == 0: major_index = i
            if val == nums[major_index]: core_sum += 1
            else: core_sum -= 1
            print(core_sum)
        print(core_sum)
        return nums[major_index]