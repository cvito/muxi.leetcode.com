from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return
        row, col = len(board), len(board[0])

        def dfs(row_pos, col_pos):
            if not 0 <= row_pos < row or not 0 <= col_pos < col or board[row_pos][col_pos] != 'O':
                return
            board[row_pos][col_pos] = "A"
            dfs(row_pos + 1, col_pos)
            dfs(row_pos - 1, col_pos)
            dfs(row_pos, col_pos + 1)
            dfs(row_pos, col_pos - 1)

        for i in range(row):
            dfs(i, 0)
            dfs(i, col - 1)

        for j in range(col - 1):
            dfs(0, j)
            dfs(row - 1, j)

        for i in range(row):
            for j in range(col):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

s = Solution()
#r = [["O","O","O"],["O","O","O"],["O","O","O"]]
r = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
s.solve(r)
print(r)
