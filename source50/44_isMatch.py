
# 超时
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return len(s) == 0

        def helper(s_index, p_index) -> bool:
            if p_index >= len(p) and s_index >= len(s):
                return True
            elif p_index >= len(p) and s_index < len(s):
                return p[-1] == '*'
            elif p_index < len(p) and s_index >= len(s):
                while p_index < len(p):
                    if p[p_index] != '*': return False
                    p_index += 1
                return True

            if p[p_index] == '?':
                return helper(s_index+1, p_index+1)
            elif p[p_index] == '*':
                while p_index+1 < len(p):
                    if p[p_index+1] == '*':
                        p_index += 1
                return helper(s_index, p_index+1) or helper(s_index+1, p_index)
            elif s_index < len(s) and s[s_index] == p[p_index]:
                return helper(s_index+1, p_index+1)
            return False

        return helper(0, 0)


class Solution_V2:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return len(s) == 0
        len_s, len_p = len(s), len(p)
        dp = [[False] * (len_p + 1) for _ in range(len_s + 1)]
        dp[0][0] = True
        for i in range(1, len_p+1):
            if p[i - 1] != '*':
                break
            dp[0][i] = True

        for i in range(1, len_s + 1):
            for j in range(1, len_p + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[len_s][len_p]



s = Solution()
r = s.isMatch("aa", "a**b")
print(r)