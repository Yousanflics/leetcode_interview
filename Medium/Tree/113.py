# 求所有路径和为 target 的路径，这里需要用到 dfs 了
from typing import List
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, current_sum, path):
            if not node:
                return
            current_sum += node.val
            path.append(node.val)
            if not node.left and not node.right and current_sum == targetSum:
                # path 是一直在被修改的，每次存储的都是最新的
                res.append(path.copy())
            dfs(node.left, current_sum, path)
            dfs(node.right, current_sum, path)
            # 需要回溯
            path.pop()
        dfs(root, 0, [])
        return res
