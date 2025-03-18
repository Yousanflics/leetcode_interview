from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root:TreeNode):
        if not root:
            return []
        result = []
        queue = deque([root])

        left_to_right = True

        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if not left_to_right:
                level_nodes.reverse()

            result.append(level_nodes)

            left_to_right = not left_to_right
        
        return result
    
if __name__ == "__main__":
    # construct binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    s = Solution()
    result = s.zigzagLevelOrder(root)

    print("Zig Zag result:")
    for i, level in enumerate(result):
        direction = "left to right" if i % 2 == 0 else "right to left"
        print(f"Level {i + 1} {direction}: {level}")
    
