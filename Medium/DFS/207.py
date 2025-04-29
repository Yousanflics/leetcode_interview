# Course Schedule
# 这题的本质是一个有向图中是否存在环的算法，通常用于解决课程安排问题
# graph: 构建领接表，表示图；关于图可以有领接表和领接矩阵两种方式一般稀疏矩阵用领接表会更高效一点

"""
graph = [[] for _ in range(numCourses)] 创建大小为 numCourses 邻接表数组
for dest, src in prerequisites: src-> 前置， dest-> 需要完成的，后置
    graph[src].append(dest) 表示 src 指向 dest 的边

visited = [0] * numCourses 使用数组记录每个节点的访问状态 0 未访问 1 这个在访问 2 访问完成

dfs 实现：
def dfs(node):
    if visited[node] == 1:
        return False
    if visited[node] == 2:
        return True
    visited[node] = 1
    for neighbor in graph[node]:
        if not dfs(neighbor):
            return False
    visited[node] = 2
    return True

如果遇到状态为 1 的 node，说明当前路径已经访问过这个 node 存在环，返回 False
如果遇到状态为 2 的节点，说明这个 node 已经完成访问，不会构成环，返回 True
将当前 node 标记为正在访问（状态 1）
递归的方位所有的邻居后，将当前节点标记为已完成访问（状态2）并且返回 True

主函数的逻辑：
for i in range(numCourses):
    if visited[i] == 0:
        if not dfs(i):
            return False
return True

对每一个还没有访问的节点进行 DFS。如果任何一个 DFS 返回 False（发现环），则整个函数返回 False
如果所有的 DFS 都返回 True（没有环），则整个函数都返回 True

时间复杂度 O(V+E)
空间复杂度 O(V+E) 由于用的是邻接表而不是邻接图
"""

class Solution:
    def canFinish(self, numCourses, prerequisites):
        # 创建邻接表表示图（比邻接矩阵更高效）
        # 对于稀疏图领接表会比邻接矩阵更高效更节省空间
        graph = [[] for _ in range(numCourses)]
        for dest, src in prerequisites:
            graph[src].append(dest)
        
        # 3种状态：0=未访问，1=正在访问，2=已完成访问
        visited = [0] * numCourses
        
        def dfs(node):
            # 如果节点在当前DFS路径中，发现环
            if visited[node] == 1:
                return False
            # 如果节点已经被完全处理过，不需要再次处理
            if visited[node] == 2:
                return True
            
            # 标记为正在访问
            visited[node] = 1
            
            # 访问所有邻居
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            
            # 标记为已完成访问
            visited[node] = 2
            return True
        
        # 对每个未访问的节点进行DFS
        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return False
        
        return True
