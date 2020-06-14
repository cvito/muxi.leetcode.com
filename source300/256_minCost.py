from typing import List


class Solution:
    def __init__(self):
        self.dict = {}

    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 0: return 0
        c0 = self.get_min(costs, 0, 0)
        c1 = self.get_min(costs, 0, 1)
        c2 = self.get_min(costs, 0, 2)
        return min(c0, c1, c2)

    def slect_red(self, costs: List[List[int]], index: int) -> int:
        key0 = "{}-{}".format(index + 1, 0)
        if key0 in self.dict:
            c0 = self.dict[key0]
        else:
            c0 = self.get_min(costs, index + 1, 0)
            self.dict[key0] = c0
        return c0

    def slect_bule(self, costs: List[List[int]], index: int) -> int:
        key1 = "{}-{}".format(index + 1, 1)
        if key1 in self.dict:
            c1 = self.dict[key1]
        else:
            c1 = self.get_min(costs, index + 1, 1)
            self.dict[key1] = c1
        return c1

    def slect_green(self, costs: List[List[int]], index: int) -> int:
        key2 = "{}-{}".format(index + 1, 2)
        if key2 in self.dict:
            c2 = self.dict[key2]
        else:
            c2 = self.get_min(costs, index + 1, 2)
            self.dict[key2] = c2
        return c2

    def get_min(self, costs: List[List[int]], index: int, c_type: int) -> int:
        if index == len(costs)-1: return costs[index][c_type]
        if c_type == 0:
            c1 = self.slect_bule(costs, index)
            c2 = self.slect_green(costs, index)
            return costs[index][0] + min(c1, c2)
        if c_type == 1:
            c0 = self.slect_red(costs, index)
            c2 = self.slect_green(costs, index)
            return costs[index][1] + min(c0, c2)
        if c_type == 2:
            c0 = self.slect_red(costs, index)
            c1 = self.slect_bule(costs, index)
            return costs[index][2] + min(c0, c1)
        return 0

s = Solution()
print(s.minCost([[17,2,17],[16,16,5],[14,3,19]]))