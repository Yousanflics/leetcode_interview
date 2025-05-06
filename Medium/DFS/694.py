# num of distinct islands


"""
重点需要搞清楚两个点，绝对坐标和相对坐标
"""

from typing import List

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        row, col = len(grid), len(grid[0])
        shapes = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        def dfs(x, y, pos, island_directions):
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0<=nx<row and 0<=ny<col and grid[nx][ny] and (nx, ny) not in visited:
                    temp_direction = (pos[0]+dx, pos[1]+dy)
                    visited.add((nx, ny))
                    island_directions.append(temp_direction)
                    dfs(nx, ny, temp_direction, island_directions)
            return tuple(island_directions)


        for x in range(row):
            for y in range(col):
                if grid[x][y] and (x, y) not in visited:
                    # 这两行的顺序不可以交换，交换了可能会导致无限 DFS 递归
                    visited.add((x,y))
                    shapes.add(dfs(x, y, (0, 0),[(0,0)]))
        return len(shapes)

