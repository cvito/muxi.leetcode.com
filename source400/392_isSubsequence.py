import bisect


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_next_index = 0
        s_find_count = 0
        for v in s:
            if t_next_index >= len(t): break
            for i in range(t_next_index, len(t)):
                t_next_index = i + 1
                if t[i] == v:
                    s_find_count += 1
                    break
        print(s_find_count)
        if s_find_count == len(s): return True
        return False

class Solution_V2:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t: return True
        if len(s) > len(t): return False
        res_size, t_pos = 0, 0
        for i in range(len(s)):
            while t_pos < len(t):
                val = t[t_pos]
                t_pos += 1
                if val == s[i]:
                    res_size += 1
                    break
        return res_size == len(s)

s = Solution_V2()
r = s.isSubsequence("", "")
print(r)