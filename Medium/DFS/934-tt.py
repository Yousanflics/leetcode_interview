# Shortest Bridge
from typing import List
from collections import deque

"""
思路简单介绍：
使用深度优先搜索 (DFS) 找到并标记第一个岛屿（将值从 1 改为 2）
将第一个岛屿的所有单元格加入队列
使用广度优先搜索 (BFS) 逐层向外扩展，直到找到第二个岛屿：

如果找到值为 1 的单元格，说明到达了第二个岛屿，返回当前距离
如果找到值为 0 的水域单元格，将其标记为 -1（表示已访问）并加入队列
每处理完一层后，距离加 1



这个解决方案的时间和空间复杂度都是 O(n²)，其中 n 是网格的维度。
"""
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(i, j, queue):
            # 保证在边界内
            if not (0 <= i < n and 0 <= j < n) or grid[i][j] != 1:
                return
            grid[i][j] = 2
            queue.append((i, j))

            for di, dj in directions:
                dfs(i+di, j+dj, queue)

        queue = deque()
        found = False

        for i in range(n):
            if found:
                break
            for j in range(n):
                # 第一个岛
                if grid[i][j] == 1:
                    # 继续向外找到当前这个岛的剩余部分
                    dfs(i, j, queue)
                    found = True
                    break
        
        distance = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    # 防止遍历方向超出边界
                    if 0 <= ni < n and 0 <= nj < n:
                        if grid[ni][nj] == 1:
                            return distance
                        if grid[ni][nj] == 0:
                            grid[ni][nj] = -1
                            queue.append((ni, nj))

            distance += 1
        return -1

