# nums of islands
from typing import List
class Solution:
    def numOfIslands(grid: List[List[str]]) -> int:
        if not grid:
            return
        row, col = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            if not (0<i<row and 0<j<col) or grid == '0':
                return
            grid[i][j] = '0'
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count
