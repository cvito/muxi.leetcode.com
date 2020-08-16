from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row_len, col_len = len(image), len(image[0])
        dest_color = image[sr][sc]
        visited = {}
        def helper(r_idx, c_idx):
            if r_idx < 0 or r_idx >= row_len:
                return
            elif c_idx < 0 or c_idx >= col_len:
                return

            if (r_idx, c_idx) in visited:
                return
            visited[(r_idx, c_idx)] = True
            if image[r_idx][c_idx] != dest_color:
                return

            image[r_idx][c_idx] = newColor
            helper(r_idx-1, c_idx)
            helper(r_idx+1, c_idx)
            helper(r_idx, c_idx-1)
            helper(r_idx, c_idx+1)
            return

        helper(sr, sc)
        return image

s = Solution()
r = s.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
print(r)

