from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        if not A or not B: return 0
        dp = {}
        for i, v in enumerate(B):
            if v in dp:
                dp[v].append(i)
            else:
                dp[v] = [i]
        max_rsp = 0
        for i in range(len(A)):
            val_a = A[i]
            if val_a not in dp: continue
            for j in dp[val_a]:
                index_a, index_b = i+1, j+1
                ans = 1
                while index_a < len(A) and index_b < len(B):
                    if A[index_a] != B[index_b]: break
                    ans += 1
                    index_a += 1
                    index_b += 1
                max_rsp = max(max_rsp, ans)
                if max_rsp >= len(A)-i: return max_rsp
        return max_rsp

class Solution_V2:
    def findLength(self, A: List[int], B: List[int]) -> int:
        if not A or not B: return 0
        max_rsp = 0
        dp = [[0]*len(B) for _ in A]
        for i in range(len(A)-1, -1, -1):
            for j in range(len(B)-1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1]+1 if i < len(A)-1 and j < len(B)-1 else 1
                    max_rsp = max(max_rsp, dp[i][j])
                else:
                    dp[i][j] = 0
        return max_rsp


s = Solution_V2()
rsp = s.findLength([1,2,3,2,1], [3,2,1,4,7])
print(rsp)


