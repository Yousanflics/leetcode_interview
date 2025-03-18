from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder:List[int], inorder:List[int]):
        inorder_map = {val: idx for idx, val in enumerate(preorder)}
        def build(prestart, preend, instart, inend):
            if prestart > preend:
                return None
            root_val = preorder[prestart]
            root = TreeNode(root_val)
            root_index = inorder_map[root_val]
            left_size = root_index - instart
            root.left = build(prestart+1, prestart+left_size, instart, root_index-1)
            root.right = build(prestart+left_size+1, preend, root_index+1, inend)
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

