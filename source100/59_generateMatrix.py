from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        rsp_list = [[0] * n for _ in range(n)]
        i, j = 0, 0
        direction = ("right", "bottom", "left", "top")
        cur_dire = direction[0]
        for num in range(1, n**2+1):
            if cur_dire == direction[0]:
                # right
                if j < n and rsp_list[i][j] == 0:
                    rsp_list[i][j] = num
                    j += 1
                else:
                    cur_dire = direction[1]
                    j -= 1
                    i += 1
                    rsp_list[i][j] = num
                    i += 1
            elif cur_dire == direction[1]:
                # bottom
                if i < n and rsp_list[i][j] == 0:
                    rsp_list[i][j] = num
                    i += 1
                else:
                    cur_dire = direction[2]
                    i -= 1
                    j -= 1
                    rsp_list[i][j] = num
                    j -= 1
            elif cur_dire == direction[2]:
                # left
                if j >= 0 and rsp_list[i][j] == 0:
                    rsp_list[i][j] = num
                    j -= 1
                else:
                    cur_dire = direction[3]
                    j += 1
                    i -= 1
                    rsp_list[i][j] = num
                    i -= 1
            elif cur_dire == direction[3]:
                # top
                if i >= 0 and rsp_list[i][j] == 0:
                    rsp_list[i][j] = num
                    i -= 1
                else:
                    cur_dire = direction[0]
                    i += 1
                    j += 1
                    rsp_list[i][j] = num
                    j += 1
        return rsp_list


s = Solution()
r = s.generateMatrix(3)
print(r)

