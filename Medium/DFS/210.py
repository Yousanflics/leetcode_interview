# Course Schedule II
# 经典的拓扑排序题目，要求给满足前置要求的课程安排顺序 list 没有的话返回 []
# Course Schedule I 只需要判断是否满足，即判断有向图里面是否有环，
# 这里为了更高效的创建领接表引入了 defaultdict 需要引入 collections 里面的 defaultdict，同时因为是 BFS 所以需要借助 queue

from collections import deque, defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degrees = [0] * numCourses
        for dest, req in prerequisites:
            graph[req].append(dest)
            in_degrees[dest] += 1
        
        queue = deque()
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)

        res = []
        
        while queue:
            cur = queue.popleft()
            res.append(cur)

            for des in graph[cur]:
                in_degrees[des] -= 1
                if in_degrees[des] == 0:
                    queue.append(des)
        return res if len(res) == numCourses else []
    
    def findOrderByDFS(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 构建邻接表
        graph = defaultdict(list)
        for des, src in prerequisites:
            graph[src].append(des)
        # 0 没有访问 1 正在访问 2 完成访问
        visited = [0]* numCourses
        res = []
        # 检测环
        def dfs(course):
            if visited[course] == 1:
                return False
            if visited[course] == 2:
                return True
            
            visited[course] = 1
            for next in graph[course]:
                if not dfs(next):
                    return False

            visited[course] = 2
            res.append(course)
            return True
        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return []
        return res[::-1]
    
"""
DFS 方法：

构建图：

创建邻接表表示课程之间的依赖关系


DFS 过程：

使用状态数组跟踪每个课程的访问状态（未访问/正在访问/已完成）
对每个未访问的课程进行 DFS
在 DFS 过程中，如果发现正在访问的课程被再次访问，说明存在环路
在访问完一个课程的所有后续课程后，将该课程标记为已完成，并加入结果


反转结果：

由于 DFS 是后序遍历(post order)，需要将结果反转才能获得正确的学习顺序
本质是因为 DFS 相当于是栈的操作流程所以需要后进的先出



复杂度分析

时间复杂度：O(V + E)，其中 V 是节点数（课程数），E 是边数（先修关系数）
空间复杂度：O(V + E)，用于存储图和访问状态
"""

