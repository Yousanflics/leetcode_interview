# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        self.pre, self.first, self.second = None, None, None
        self.inOrder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
    
    def inOrder(self, root: TreeNode):
        if not root: return
        self.inOrder(root.left)
        if self.pre and self.pre.val > root.val:
            if not self.first:
                self.first = self.pre
            self.second = root
        self.pre = root
        self.inOrder(root.right)


二叉搜索树  BST  有一个性质：
中序遍历（inorder traversal）是严格递增的，即：
左子树 -> root -> 右子树
会按照从小到大的顺序方位所有的节点
问题：BST 中有两个节点被错误的交换了位置，导致中序遍历不再是严格递增
算法思路：
由于 BST 中序应该是递增的，如果两个节点被交换了，我们会在中序遍历的时候发现两处下降的位置
1. 第一个错误点 first：第一个你需对出现的较大值（即 pre.val > root.val)
2. 第二个错误点 second：第二个你需对出现的较小值（即second.val < root.val)
examples:
错误 BST：
     3
    / \
   1   4
      /
     2
正确 BST 应该是：
     2
    / \
   1   4
      /
     3

代码中的 self.pre 记录上一个遍历的节点，用于检测逆序
由于这里要求只能是 O(n) 因此这里似乎只能是递归的解决方式

