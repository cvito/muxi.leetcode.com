import bisect
from typing import List


# 暴力 O(N*N)
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0
        len_nums = len(nums)
        len_min = len_nums+1
        for i in range(len_nums):
            if nums[i] >= s: return 1
            sum_num = nums[i]
            for j in range(i+1, len_nums):
                sum_num += nums[j]
                if sum_num >= s:
                    len_min = min(j-i+1, len_min)
                    break
        return 0 if len_min == len_nums+1 else len_min


# 采用二分查找方式
class Solution_V2:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0
        sums = [0]
        for v in nums:
            sums.append(sums[-1]+v)
        print("sums", sums)
        len_nums = len(nums)
        len_min = len_nums + 1
        for i in range(1, len_nums+1):
            target = s + sums[i-1]
            pos = bisect.bisect_left(sums, target)
            print("i:{}, target:{}, pos:{}".format(i, target, pos))
            if pos <= len_nums:
                len_min = min(len_min, pos-(i-1))
        return 0 if len_min == len_nums + 1 else len_min



s = Solution_V2()
print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
