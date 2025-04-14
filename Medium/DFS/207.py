class Solution:
    def canFinish(self, numCourses, prerequisites):
        # 创建邻接表表示图（比邻接矩阵更高效）
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
