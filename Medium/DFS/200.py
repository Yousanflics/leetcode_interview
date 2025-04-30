# nums of islands
from typing import List
class Solution:
    def numOfIslands(grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        row, col = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            # 如果是非1区域直接返回，就不看了，那么剩下的就是 1
            if not (0<= i <row and 0<= j <col) or grid == '0':
                return
            # 重新标记为 0 表示已经访问过了，这个标记非常重要
            grid[i][j] = '0'
            #上下左右四个角度去 dfs
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        for i in range(row):
            for j in range(col):
                # 对不是 0 也就是只是 1 的位置进行访问，
                if grid[i][j] == '1':
                    # 这个 count 的位置是正确的，这是岛屿 1 起始位置因为不是 1 的话 dfs 会直接返回也就不会 count ++
                    count += 1
                    dfs(i, j)
        return count
