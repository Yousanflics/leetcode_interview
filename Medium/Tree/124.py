# max path sum in binary tree

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
查找二叉树中的任意路径的最大和，这里的任意路径不一定要经过根节点
这里考虑递归的思想，定义了 maxend 函数，以当前 node 为端点的最大路径和
1、更新全局最大路径和（可能穿过当前节点）
2、返回以当前节点为端点的最大路径和（用于上层计算）
"""

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def maxend(node):
            if not node:
                return 0
            
            left = maxend(node.left)
            
            right = maxend(node.right)
            
            self.max = max(self.max, left + node.val + right)
            
            return max(node.val + max(left, right), 0)
        #初始化这里的 self.max 标记位
        self.max = float('-inf')
        maxend(root)
        return self.max
