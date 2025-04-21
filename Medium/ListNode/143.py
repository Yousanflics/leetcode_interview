class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# 时间复杂度为 O(n)
# 空间复杂度为 O(1)
class Solution:
    def reorderList(self, head: ListNode) -> None:
        # 整个过程可以分为 3 步走
        if not head or not head.next or not head.next.next:
            return
        
        # 第一步：找到链表重点
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        # breakup listnode
        slow.next = None
        # 第二步：翻转第二部分链表
        prev = None
        current = second_half
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        reversed_second_half = prev
        # 第三步：交叉合并两部分链表
        first = head
        second = reversed_second_half
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2


