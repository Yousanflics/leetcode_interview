# reverse listnode
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def reverseListRecursively(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # 一直递归到最后
        new_head = self.reverseListRecursively(head.next)
        head.next.next = head
        head.next = None
        return new_head
    
    def reverseListLiteratively(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
