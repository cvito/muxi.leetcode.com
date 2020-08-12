class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        zero_size, one_size = 0, 0
        pre_char = ''
        for i in range(len(s)):
            if zero_size and one_size and s[i] != pre_char:
                res += min(zero_size, one_size)
                if pre_char == '0': one_size = 0
                else: zero_size = 0
            if s[i] == '0': zero_size += 1
            else: one_size += 1
            pre_char = s[i]
            if i == len(s)-1 and zero_size and one_size:
                res += min(zero_size, one_size)
        return res

s = Solution()
r = s.countBinarySubstrings("00110011")
print(r)
