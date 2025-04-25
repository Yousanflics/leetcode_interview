# 199 是右边看的右视图，也就是打印层序遍历最右边的这个元素，现在给出变式
# 我要左边的视图 tt 面试中又出现过的
from typing import Optional, List

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    # dfs solution
    def leftSideView(self, root: Optional[TreeNode]) -> List[TreeNode]:
        if not root:
            return []
        res = []
        def dfs(node, level):
            if not node:
                return
            if level == len(res):
                res.append(node.val)
            # 如果是 right 的话简答的修改这一部分就好了，换个顺序
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root, 0)
        return res
        
