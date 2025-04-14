# Right side view of Binary Tree
from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        def dfs(node: Optional[TreeNode], depth: int):
            if not node:
                return
            if depth == len(result):
                result.append(node.val)
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)
        dfs(root, 0)
        return result
