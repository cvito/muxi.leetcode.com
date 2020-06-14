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