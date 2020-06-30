from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        res = [[]]
        for num in nums:
            res += [curr + [num] for curr in res]
        return res


class Solution_V2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(path, used):
            res.append(path)
            for num in nums:
                if num in used and used[num]: continue
                used[num] = True
                helper([path+str(num)], used)
                #used[num] = False

        res = []
        path_size_dict = {}
        helper([], {})
        return res

s = Solution_V2()
rsp = s.subsets([1,2,3])
print(rsp)