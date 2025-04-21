
from typing import Optional
# 这里要注意 116 是一个完美二叉树跟 117 的前提是不一样的

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def connect(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.left:
            return root
        root.left.next = root.right
        # 递归的过程中会用到前面已经设置了 next 指针指向的位置
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root
