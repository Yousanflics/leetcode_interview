# number of islands
# 经典的 dfs 和 bfs 问题，求连通区域的个数
# 1 DFS
# 遍历整个网格，每当遇到1时，说明发现了一个新的岛屿，岛屿的数量 count += 1 使用 dfs 递归遍历当前岛屿的所有陆地各自，并且将访问过的1标记位 0 避免重复计算，递归终止条件，当递归访问到越界的位置或者水域 ‘0’ 时停止递归
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r,c):
            if r < 0 or c < 0 or r>=rows or c>cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r,c)
        return count
