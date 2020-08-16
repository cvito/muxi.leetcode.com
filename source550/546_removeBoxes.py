from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        dp = [[[0]*100 for _ in range(100)] for _ in range(100)]
        def helper(left, right, k) -> int:
            if left > right: return 0
            print("left:{}, right:{}, k:{}".format(left, right, k))
            if dp[left][right][k] != 0: return dp[left][right][k]
            while left < right and boxes[right] == boxes[right-1]:
                right -= 1
                k += 1

            dp[left][right][k] = helper(left, right-1, 0) + (k+1)**2
            for i in range(left, right):
                if boxes[i] == boxes[right]:
                    dp[left][right][k] = max(dp[left][right][k], helper(left, i, k+1) + helper(i+1, right-1, 0))
            return dp[left][right][k]
        return helper(0, len(boxes)-1, 0)

s = Solution()
r = s.removeBoxes([1,3,2,2,2,3,4,3,1])
print(r)