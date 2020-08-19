#参考文档：https://segmentfault.com/a/1190000003914228

class Solution:
    def countSubstrings(self, s: str) -> int:
        #添加特殊符号，使得整个字符串长度恒为奇数
        s = "#" + "#".join(s) + "#"

        #表示整个回文串最大的下标位置
        max_right = 0

        #表示以pos为对称轴得到max_right
        pos = 0

        #结果返回值
        res = 0

        dp = [0] * len(s)
        for i in range(len(s)):
            #(2*pos-i)是求出以pos为对称轴，i的对称半径位置j的dp[j]
            dp[i] = 1 if i > max_right else min(dp[2*pos - i], max_right - i + 1)

            while i-dp[i] >= 0 and i+dp[i] < len(s) and s[i-dp[i]] == s[i+dp[i]]:
                dp[i] += 1

            #若回文串半径位置比max大，更新max
            if dp[i] + (i-1) > max_right:
                max_right = dp[i] + (i-1)
                pos = i

            #半径长度每一个位置都是算为一个回文串
            res += (dp[i]) // 2
        return res

s = Solution()
r = s.countSubstrings("abc")
print(r)


