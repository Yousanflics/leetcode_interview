class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre, curr = head, head.next
        while curr:
            if curr.val >= pre.val:
                pre = curr
            else:
                temp = dummy
                while temp.next.val < curr.val:
                    temp = temp.next
                # break first
                pre.next = curr.next
                curr.next = temp.next
                temp.next = curr
            
            curr = pre.next
        return dummy.next


