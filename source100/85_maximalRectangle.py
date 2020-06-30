from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        max_rsp = 0
        dp = [[0]*len(matrix[0]) for _ in matrix]
        for i in range(len(matrix) ):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0": continue
                width = dp[i][j] = dp[i][j-1] + 1 if j else 1
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    max_rsp = max(max_rsp, width * (i - k + 1))
        return max_rsp

s = Solution()
rsp = s.maximalRectangle([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
])
print(rsp)
