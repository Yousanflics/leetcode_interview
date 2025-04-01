# max path sum in binary tree

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def maxend(node):
            if not node:
                return 0
            
            left = maxend(node.left)
            
            right = maxend(node.right)
            
            self.max = max(self.max, left + node.val + right)
            
            return max(node.val + max(left, right), 0)
        
        self.max = float('-inf')
        maxend(root)
        return self.max
