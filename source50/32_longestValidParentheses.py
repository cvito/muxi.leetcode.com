class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        def helper(index, depth) -> int:
            if index >= len(s) or depth < 0: return 0
            if s[index] == '(': return helper(index+1, depth+1)
            if depth == 0: return helper(index+1, depth)
            return 2 + helper(index+1, depth-1)
        return helper(0, 0)


#有效最长串（动态规划）
class Solution_V2:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        dp = [0] * len(s)
        for i in range(len(s)):
            if s[i] == ')' and i - dp[i-1] -1 >= 0 and s[i - dp[i-1] -1] == '(':
                dp[i] = dp[i-1] + dp[i - dp[i-1] -2] + 2
        return max(dp)

# 有效最长串（栈）
class Solution_V3:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        max_len, cur_len = 0, 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
                continue
            if stack[-1] >= 0 and s[stack[-1]] == '(':
                stack.pop()
                top = stack[-1] if len(stack) != 0 else 0
                cur_len = i - top
                max_len = max(max_len, cur_len)
                continue
            stack.append(i)
        return max_len







s = Solution_V3()
r = s.longestValidParentheses(")()())()()(")
print(r)

