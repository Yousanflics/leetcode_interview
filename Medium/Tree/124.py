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

二叉树中的路径可以分为两类：
- 单边路径：路径从某个节点出发，沿着左或右子树单向延伸（例如 父节点 → 左子节点 → 左孙子节点）。
- 跨越根节点的路径：路径以某个节点为顶点，同时包含其左右子树的部分（例如 左子节点 → 父节点 → 右子节点）。

时间复杂度 O(n)
空间复杂度 O(h) h 是树的高度
"""

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def max_gain(node):
            if not node:
                return 0
            
            left = max(max_gain(node.left), 0)
            
            right = max(max_gain(node.right), 0)
            
            # 当前节点作为路径的最高点时的路径和
            # ！！！需要显示更新 self.max 这种考虑到了左右两个path一起的情况，其他的递归都只是某一条路径
            self.max = max(self.max, left + node.val + right)
            
            # 往左边或者右边
            return node.val + max(left, right)
        #初始化这里的 self.max 标记位
        self.max = float('-inf')
        max_gain(root)
        return self.max
