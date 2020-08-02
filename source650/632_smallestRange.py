import heapq
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        range_left, range_right = -10**9, 10**9
        max_value = max(val[0] for val in nums)
        priority_queue = [(val[0], i, 0) for i, val in enumerate(nums)]
        heapq.heapify(priority_queue)
        while True:
            min_value, row, idx = heapq.heappop(priority_queue)
            if max_value - min_value < range_right - range_left:
                range_right, range_left = max_value, min_value
            if idx == len(nums[row])-1:
                break
            max_value = max(max_value, nums[row][idx+1])
            heapq.heappush(priority_queue, (nums[row][idx+1], row, idx+1))
        return [range_left, range_right]

s = Solution()
r = s.smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]])
print(r)