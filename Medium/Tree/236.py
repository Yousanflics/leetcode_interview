class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncester(self, root: 'TreeNode', p : 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncester(root.left, p, q)
        right = self.lowestCommonAncester(root.right, p, q)

        if left and right:
            return root
        
        return left if left else right

"""
    3
   / \
  5   1
 / \ / \
6  2 0  8
  / \
 7   4

情况1：寻找5和1的LCA

在节点3，我们递归搜索左子树和右子树
左子树递归到节点5，发现就是p，直接返回5
右子树递归到节点1，发现就是q，直接返回1
回到节点3，左右子树分别返回了5和1，说明5和1在3的两侧，所以3是LCA

情况2：寻找5和4的LCA

在节点3，递归搜索左右子树
左子树递归到节点5：

递归到节点6，返回null
递归到节点2：

递归到节点7，返回null
递归到节点4，返回4（因为它是q）
节点2的left=null，right=4，所以返回4


节点5的left=null，right=4，现在的情况类似"找到了一个节点，另一个节点在其子树中"
但是5本身就是p，所以node==p条件满足，直接返回5


右子树递归到节点1，没找到p或q，返回null
回到节点3，left=5，right=null，所以返回5作为LCA

关键点
这种算法的巧妙之处在于：

如果p和q其中之一是另一个的祖先，那么第一个被找到的就是LCA
如果p和q在不同的子树中，那么它们的分叉点就是LCA
递归的返回值只可能是：null、p、q或者p和q的LCA

这种递归设计使得算法既简洁又高效，能够在一次树的遍历中找到答案。
"""
