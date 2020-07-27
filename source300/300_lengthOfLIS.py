import bisect
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dp = [0] * (n-1) + [1]
        res = 1
        for i in range(n-2, -1, -1):
            for j in range (i+1, n):

                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1)
                    continue
                dp[i] = max(dp[i], 1 + dp[j]) if nums[j] > nums[i] else max(dp[i], dp[j])
                res = max(res, dp[i])
        return res

class Solution_V2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        lis = []
        for v in nums:
            pos = bisect.bisect_left(lis, v)
            if pos >= len(lis): lis.append(v)
            else: lis[pos] = v
        return len(lis)

s = Solution_V2()
#r = s.lengthOfLIS([10,9,2,5,3,7,101,18]) #4
#r = s.lengthOfLIS([2,2])  #1
#r = s.lengthOfLIS([10,9,2,5,3,4]) #3
r = s.lengthOfLIS([1,3,6,7,9,4,10,5,6]) #6
print(r)