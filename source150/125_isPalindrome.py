class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: return True
        l, r = 0, len(s)-1
        while l < r:
            if not s[l].isdigit() and not s[l].isalpha():
                l += 1
                continue
            if not s[r].isdigit() and not s[r].isalpha():
                r -= 1
                continue
            if s[l].lower() != s[r].lower(): return False
            else: l += 1; r -= 1
        return True

s = Solution()
res = s.isPalindrome("b man, a plan, a canal: Panama")
print(res)