class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        node = root
        queue = []
        while True:
            while node:
                queue.append(node)
                node = node.left
            
            #从 list 的尾部拿数据相当于栈顶
            node = queue.pop()
            k -= 1
            if k == 0:
                return node.val
            else:
                node = node.right
