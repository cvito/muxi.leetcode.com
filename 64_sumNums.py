class Solution:
    def sumNums(self, n: int) -> int:
        ans = 0
        def helper(num) -> bool:
            nonlocal ans
            ans += num
            return num > 0 and helper(num-1)
        helper(n)
        return ans

s = Solution()
r = s.sumNums(6)
print(r)