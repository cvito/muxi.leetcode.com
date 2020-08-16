class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[0:n]

s = Solution()
r = s.reverseLeftWords("abcdefg", 2)
print(r)