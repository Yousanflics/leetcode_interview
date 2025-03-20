# invert Binary Tree 翻转二叉树
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return self.iter(root)

    def recur(self, root):
        if root:
            root.left, root.right = self.recur(root.right), self.recur(root.left)
            return root
    def iter(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += [node.left, node.right]
        return root
