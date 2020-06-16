from typing import List

#水平横扫暴力法
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        res = strs[0]
        for i in range(1, len(strs)):
            if res == "": break
            for j in range(min(len(strs[i]), len(res))):
                if strs[i][j] != res[j]: res = res[:j]; break
            if len(res) > len(strs[i]): res = res[:len(strs[i])]
            if not res: break
        return res

#分治思路
class Solution_V2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        return self.get_prefix(strs, 0, len(strs)-1)

    def get_prefix(self, strs, l, r) -> str:
        if l == r: return strs[l]
        mid = (l + r) // 2
        left_pre = self.get_prefix(strs, l, mid)
        right_pre = self.get_prefix(strs, mid+1, r)
        return self.comp_prefix(left_pre, right_pre)

    def comp_prefix(self, left, right) -> str:
        if not left or not right: return ""
        for i in range(min(len(left), len(right))):
            if left[i] != right[i]: return left[:i]
        return right if len(left) > len(right) else left




s = Solution_V2()
str1 = s.longestCommonPrefix(["flo", "f"])
print(str1)