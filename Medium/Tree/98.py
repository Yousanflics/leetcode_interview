# Validate a BST

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode):
        self.prev = None

        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if self.prev and self.prev.val >= root.val:
                return False
            self.prev = root

            return inorder(root.right)
        return inorder(root)
