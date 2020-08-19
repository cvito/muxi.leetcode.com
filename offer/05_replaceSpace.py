class Solution:
    def replaceSpace(self, s: str) -> str:
        i = 0
        while i < len(s):
            if s[i] != " ":
                i += 1
            else:
                s = s[:i] + "%20" + s[i+1:]
                i += 3
        return s

s = Solution()
r = s.replaceSpace("We are happy.")
#r = s.replaceSpace("    ")
print(r)