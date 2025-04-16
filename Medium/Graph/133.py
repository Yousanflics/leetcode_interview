# Graph clone

from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        # clone node 中最重要的是这里的 visited 标记，不能重复复制 node
        visited = {}
        clone_node = Node(node.val, [])
        def dfs(org_node:'Node'):
            if not org_node:
                return None
            if org_node in visited:
                return visited[org_node]
            clone_node = Node(org_node.val, [])
            visited[org_node] = clone_node

            for neighbor in org_node.neighbors:
                clone_node.neighbors.append(neighbor)
            return clone_node
        return dfs(node)

