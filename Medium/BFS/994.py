# 多源头 bfs: 橘子烂完的时间
# bfs 往往考虑有  queue 来辅助解决

"""

初始化阶段：

创建一个队列用于BFS，初始包含所有腐烂的橘子
统计新鲜橘子的数量
如果没有新鲜橘子，直接返回0（不需要时间）


BFS过程：

使用queue存储腐烂的橘子坐标
每次处理当前队列中的所有橘子，这表示"一分钟"内的传播
对每个腐烂的橘子，检查四个方向是否有新鲜橘子
如果有，将其标记为腐烂，减少新鲜橘子计数，并加入队列


结束条件：

当队列为空（无法继续腐烂）或新鲜橘子数量变为0时，BFS结束
如果还有剩余的新鲜橘子，返回-1
否则返回经过的分钟数


时间复杂度: O(rows x cols) 最坏的情况下每一个都需要访问一遍
空间复杂度: O(rows x cols) 最坏的情况下对重包含所有网格中的所有单元格

"""
from collections import deque
from typing import List

class Solution:
    def orangeRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.app((r,c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        # 开局已经全部烂掉
        if fresh_count == 0:
            return 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        minutes = 0
        
        # 开始 bfs
        while queue and fresh_count > 0:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))
            # queue 遍历一次才算 1 minute
            minutes += 1
        return -1 if fresh_count > 0 else minutes
