import functools
from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        #通过异或先找出两个不同的数字
        res = functools.reduce(lambda x, y: x ^ y, nums)
        # res = 0
        # for num in nums:
        #     res ^= num

        #通过找到最高位不是0的
        h = 1
        while res & h == 0:
            h <<= 1

        #分组
        a, b = 0, 0
        for num in nums:
            if num & h:
                a ^= num
            else:
                b ^= num
        return [a, b]

s = Solution()
r = s.singleNumbers([1,2,5,2])
print(r)