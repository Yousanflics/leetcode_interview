class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# 两种方法
# 递归，中序遍历得到 res[] 返回 res[k-1]
# 迭代，也是广度遍历吧，辅助空间 queue
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

    
    def kthSmallestRecur(self, root: TreeNode, k: int) -> int:
        #利用特性，BST 中序遍历是一个递增序列
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder[node.right]
        return inorder(root)[k-1]
