from typing import List


# 超时
class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0: return []
        rsp_dict={}
        def helper(index, path_sum):
            if index == k: rsp_dict[path_sum] = True
            else:
                helper(index+1, path_sum+shorter)
                helper(index+1, path_sum+longer)
            return
        helper(0, 0)
        return [k for k in rsp_dict]



class Solution_V2:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0: return []
        if shorter == longer: return [shorter*k]
        rsp = [0]*(k+1)
        for i in range(0, k+1):
            rsp[i] = shorter*(k-i) + longer*i
        return rsp