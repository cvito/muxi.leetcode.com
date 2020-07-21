import bisect
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)

s = Solution()
r = s.searchInsert([1,3,5,6], 0)
print(r)