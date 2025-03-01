# partition listnode: 小的都在 x 的前面大的保持位置不变
# 说一个关于链表分割，重构或者合并时候使用 dummy node（虚拟头节点）通常是更好的
# 选择，这样可以简化代码的逻辑，避免特殊的逻辑（比如空链表或者第一个元素的特殊处理）让代码更具有可读性和鲁棒性
#definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l2.next = None
        l1.next = l2.next
        return l1.next
