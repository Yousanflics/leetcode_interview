class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return None
        if(max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif(min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        
    def lowestCommonAncestor1(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None
        if(max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor1(root.left, p, q)
        elif(min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor1(root.right, p, q)
        # p,q 在 root 两侧
        else:
            return root
