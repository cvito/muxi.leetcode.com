from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        if not nums: return 0
        dict = {}
        for v in nums:
            if v in dict: return v
            dict[v] = True
        return 0
