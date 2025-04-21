# Surrounded regions
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 首先考虑 dfs 遍历方式，在 board 本身修改，因此不考虑引入 visited set 的操作
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != 'O':
                return
            
            # 临时标记，这个 'O' 跟边界相连
            board[r][c] = 'T'
            
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
            
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and (i == 0 or i == rows - 1 or j == 0 or j == cols - 1):
                    dfs(i, j)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
