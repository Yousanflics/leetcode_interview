# Dependency Analyzer

from collections import defaultdict, deque

class DependencyAnalyzer:
    def __init__(self):
        self.graph = defaultdict(list)
        self.nodes = set()
    # dependent rely on dependency
    def add_dependency(self, dependent, dependency):
        self.graph[dependent].append(dependency)
        self.nodes.add(dependent)
        self.nodes.add(dependency)

    def detect_cycle_dfs(self):
        #visited dic
        visited = {node:0 for node in self.nodes}
        self.cycle_path = []
        def dfs(node, path):
            visited[node] = 1
            path.append(node)

            for neighbor in self.graph[node]:
                if visited[neighbor] == 0:
                    if dfs(neighbor, path):
                        return True
                elif visited[neighbor] == 1:
                    start_idx = path.index(neighbor)
                    self.cycle_path = path[start_idx] + [neighbor]
                    return True
                
            path.pop()
            visited[node] = 2
            return False
    
        for node in self.nodes:
            if visited[node] == 0:
                if dfs(node, []):
                    return True
        
        return False
