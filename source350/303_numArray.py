# Your NumArray object will be instantiated and called as such:
    # obj = NumArray(nums)
    # param_1 = obj.sumRange(i,j)
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        if i < 0 : i = 0
        if j >= len(self.nums): j = len(self.nums)
        range_sum = 0
        for i in range (i, j+1):
            range_sum += self.nums[i]
        return range_sum



class NumArray_V2:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.num_dect = {}
        self.init_cache()

    def init_cache(self):
        for i, v in enumerate(self.nums):
            if i-1 in self.num_dect: self.num_dect[i] = self.num_dect[i-1]+v
            else: self.num_dect[i] = v

    def sumRange(self, i: int, j: int) -> int:
        if j >= len(self.nums): j = len(self.nums)-1
        if i <= 0: return self.num_dect[j]
        return self.num_dect[j] - self.num_dect[i-1]
