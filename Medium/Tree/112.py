# 从 root 到 leaf 找到对应 target 的和
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    # 最直接的递归的解决代码
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        return (self.hasPathSum(root.left, targetSum- root.val) or self.hasPathSum(root.right, targetSum - root.val))
