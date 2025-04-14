# DFS 一种常见的基本的图的遍历算法，DFS 通常使用栈（显式或者隐式）递归实现/显式使用栈（迭代）实现

"""
graph = [
    [1, 2],    # 节点0的邻居是节点1和节点2
    [0, 3],    # 节点1的邻居是节点0和节点3
    [0, 3],    # 节点2的邻居是节点0和节点3
    [1, 2]     # 节点3的邻居是节点1和节点2
]
graph 使用邻接表表示
"""

def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print("Handle current node:", start)
    for neighbor in graph(start):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
