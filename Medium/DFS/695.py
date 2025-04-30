# 695 max area of island

# 三种：1.岛屿数量 2.岛屿最近距离 3.最大的岛屿
from typing import List
"""
这个跟之前的课程安排不太一样，课程安排是需要需要换，属于是定性，课程安排2是需要整个拓扑排序的完整顺序
这个跟前面的两个又不一样，这是需要有一个 max_area 记录每次每个岛最大，当前的和之前的max的

时间复杂度：O(m*n)，其中 m 和 n 分别是网格的行数和列数。最坏情况下，我们需要访问网格中的每个单元格一次。
空间复杂度：O(mn)，最坏情况下，整个网格都是陆地，递归调用栈的深度将达到 mn。
"""

    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        max_area = 0
        def dfs(i, j):
            #越界 or 不是 1（0）位置直接返回0，没有面积
            if not(0 <= i < m and 0 <= j < n) or grid!=1:
                return 0
            # 到这里就已经确定是 1了，只有 1才会走到这个位置
            grid[i][j] = 0
            return 1+dfs[i-1][j]+dfs[i+1][j]+dfs[i][j-1]+dfs[i][j+1]
        for i in range(m):
            for j in range(n):
                # 只有是岛屿才需要 dfs 去获取面积
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))

        return max_area
