# Shortest Bridge
from typing import List
from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(i, j, queue):
            if not (0 <= i < n and 0 <= j < n) or grid[i][j] != 1:
                return
            grid[i][j] = 2
            queue.append((i, j))

            for di, dj in directions:
                dfs(i+di, j+dj, queue)

        queue = deque()
        found = False
