#超时
class Solution:
    def integerBreak(self, n: int) -> int:
        def helper(num: int) -> int:
            if num <= 2: return 1
            mid = num // 2
            res_max = mid * (num-mid)
            for i in range(mid-1, 0, -1):
                res_new = i * helper(num-i)
                if res_max > res_new: break
                else: res_max = res_new
            return res_max
        return helper(n)

class Solution_V2:
    def integerBreak(self, n: int) -> int:
        if n <= 2: return 1
        dp = [0] * (n+1)
        dp[1], dp[2]= 1, 1
        for i in range(3, n+1):
            mid = i // 2
            res_max = max(mid * dp[i-mid], mid * (i-mid))
            for j in range(mid-1, 0, -1):
                res_new = max(j * dp[i-j], j * (i-j))
                if res_max > res_new: break
                else: res_max = res_new
            dp[i] = res_max
        return dp[n]



s = Solution_V2()
r = s.integerBreak(11)
print(r)