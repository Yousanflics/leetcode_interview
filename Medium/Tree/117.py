# 这一题跟 116 最大的区别就是 117 是一颗不完美的二叉树

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

# 时间复杂度都是 O(N) 但是使用已建立的 next 指针（常数空间）可以做到空间复杂度为 O(1)
class Solution:
    def connet(self, root:'Node') -> 'Node':
        if not root:
            return None
        
        leftmost = root
        while leftmost:
            curr = leftmost
            #leftmost = None
            pre = None

            while curr:
                # 处理左节点
                if curr.left:
                    if not pre:
                        leftmost = curr.left
                    else:
                        pre.next = curr.left
                    pre = curr.left
                # 处理右侧节点
                if curr.right:
                    if not pre:
                        leftmost = curr.right
                    else:
                        pre.next = curr.right
                    pre = curr.right
                curr = curr.next
        return root
