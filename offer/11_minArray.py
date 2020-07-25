from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if not numbers: return 0
        min_rsp = numbers[0]
        for i in numbers:
            min_rsp = min(min_rsp, i)
        return min_rsp

class Solution_V2:
    def minArray(self, numbers: List[int]) -> int:
        if not numbers: return 0
        left, right = 0, len(numbers)-1
        while left < right:
            mid = left + (right-left) // 2 #避免溢出
            if numbers[mid] < numbers[right]:
                right = mid
            elif numbers[mid] > numbers[right]:
                left = mid+1
            else:
                return numbers[mid]
        return numbers[left]

s = Solution_V2()
r = s.minArray([1,3,3])
print(r)