from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        def calCount(x):
            count = 0
            while x != 0:
                x &= x-1
                count += 1
            return count
        res = []
        for i in range(0, num+1):
            res.append(calCount(i))
        return res

class Solution_V2:
    def countBits(self, num: int) -> List[int]:
        x, b = 0, 1
        res = [0] * (num+1)
        while b <= num:
            while x < b and x+b <= num:
                res[x+b] = res[x] + 1
                x += 1
            x = 0
            b <<= 1
        return res

s = Solution_V2()
res = s.countBits(5)
print(res)


