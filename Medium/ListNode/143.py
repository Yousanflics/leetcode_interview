class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next or not head.next.next:
            return
        
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        # breakup listnode
        slow.next = None

        prev = None
        current = second_half
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        reversed_second_half = prev

        first = head
        second = reversed_second_half
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2


