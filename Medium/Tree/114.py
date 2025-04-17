#114 flatten binary tree to linked list
# 想让于是先前序遍历然后再组装 node

from typing import Optional

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        nodes = []

        def preorder(node):
            if not node:
                return
            nodes.append(node)
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)

        for i in range(len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i+1]
        
        if nodes:
            nodes[-1].left = None
            nodes[-1].right = None
