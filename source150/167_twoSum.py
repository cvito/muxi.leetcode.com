from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers: return []
        left, right = 0, len(numbers)-1
        while left <= right:
            left_num, right_num = numbers[left], numbers[right]
            total = left_num + right_num
            if total == target: return [left+1, right+1]
            if total < target: left += 1
            else: right -= 1
        return []

class Solution_V2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            total = numbers[left], numbers[right]
            if total == target: return [left+1, right+1]
            if total < target: left += 1
            else: right -= 1
        return []

class Solution_V3:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index = [0, len(numbers)-1]
        while index[0] < index[1]:
            if numbers[index[0]] + numbers[index[1]] < target:
                index[0] += 1
            elif numbers[index[0]] + numbers[index[1]] > target:
                index[1] -= 1
            else:
                index[0] += 1
                index[1] += 1
                return index

s = Solution()
r = s.twoSum([2, 7, 11, 15], 9)
print(r)

