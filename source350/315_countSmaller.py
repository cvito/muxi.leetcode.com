import bisect
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums: return []
        dict = {}
        for v in nums: dict[v] = 0
        bottom_list = list(dict.keys())
        bottom_list.sort()
        rsp_list = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            dict[nums[i]] += 1
            pos = bisect.bisect_left(bottom_list, nums[i])
            if not pos:
                rsp_list[i] = 0
                continue
            while pos > 0:
                num = bottom_list[pos-1]
                rsp_list[i] += dict[num]
                pos -= 1
        return rsp_list

s = Solution()
r = s.countSmaller([5,2,6,1])
print(r)



