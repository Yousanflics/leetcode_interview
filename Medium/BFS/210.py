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
