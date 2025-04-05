# delete the last n node in listnode

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

"""
快指针需要比慢指针提前 n+1 个节点，而不是 n 个节点。
因为我们需要找到倒数第 n 个节点的前一个节点才能执行删除操作
1 - 2 - 3 - 4 - 5
删除 3，倒数第 3 个，提前走 4 步
第一步:
哑节点 dummy(0)，使得链表变成 dummy(0)->1->2->3->4->5
第二步:
从 dummy 到 1，这算第一次移动
"""

def removeNthFromEnd(head, n):
    """
    :type head: ListNnode
    :type n: int
    :rtype ListNode
    """
    dummy = ListNode(0)
    dummy.next = head
    fast = dummy
    slow = dummy

    for _ in range(n + 1):
        if not fast:
            return None
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next
    
    slow.next = slow.next.next

    return dummy
