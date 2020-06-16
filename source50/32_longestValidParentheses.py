class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        res, cs = 0, []
        for v in s:
            if len(cs) > 0 and cs[-1] == '(' and v == ')':
                res += 2
                cs.pop()
            else: cs.append(v)
        return res
