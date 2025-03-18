# build binary tree with preorder and inorder
from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder:List[int], inorder:List[int]) -> Optional[TreeNode] :
        if not preorder or not inorder:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)
        root_index_inorder = inorder.index(root_val)

        left_subtree_size = root_index_inorder

        root.left = self.buildTree(preorder[1:1+left_subtree_size], inorder[:root_index_inorder])

        root.right = self.buildTree(preorder[1+left_subtree_size:], inorder[root_index_inorder+1:])

        return root
