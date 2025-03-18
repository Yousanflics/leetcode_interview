from typing import List
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, levelorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not levelorder or not inorder:
            return None
        
        root_val = levelorder[0]
        root = TreeNode(root_val)
        root_index_inorder = inorder.index(root_val)
        inorder_left = inorder[:root_index_inorder]
        inorder_right = inorder[root_index_inorder+1:]

        levelorder_left = []
        levelorder_right = []
        for val in levelorder[1:]:
            if val in inorder_left:
                levelorder_left.append(val)
            elif val in inorder_right:
                levelorder_right.append(val)
        
        root.left = self.buildTree(levelorder_left, inorder_left)
        root.right = self.buildTree(levelorder_right, inorder_right)

        return root

def inorderTraversal(root: TreeNode):
    result = []
    if root:
        result.extend(inorderTraversal(root.left))
        result.append(root.val)
        result.extend(inorderTraversal(root.right))
    return result


def levelorderTraversal(root: TreeNode):
    if not root:
        return []
    result = []
    # queue = [root]
    queue = deque([root])

    while queue:
        node = queue.popleft() #时间复杂度变成 O(1)
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

if __name__ == "__main__":
    levelorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    s = Solution()
    root = s.buildTree(levelorder, inorder)
    print("rebuild inorder:", inorderTraversal(root))
    print("rebuild levelorderTraversal:", levelorderTraversal(root))
