from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res_list = []
        def helper(depth, path, used):
            if depth == len(nums):
                res_list.append(path[:])
                return
            for v in nums:
                if v in used and used[v] is True: continue
                path.append(v)
                used[v] = True
                helper(depth + 1, path, used)
                path.pop()
                used[v] = False
            return
        helper(0, [], {})
        return res_list

s = Solution()
res = s.permute([1,2,3])
print(res)