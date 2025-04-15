# Reverse Linkedlist 2  翻转链表的 [m, n] 这一部分的链表
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        # 声明虚拟头方便直接返回结果不用在遍历的时候搞错了
        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode
        # pre 是 cur 的前一个位置所以遍历是 m - 1 的 range
        for i in range(m-1):
            pre = pre.next
        #reverse [m, n] nodes
        reverse = None
        cur = pre.next

        # 核心的引入 O(1) 空间复杂度，完成原地链表转置
        for i in range(n - m + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next

        # 把翻转之后的链表对接到原来的接口处，reverse 是翻转之后的头指针，cur 是低 n + 1 个 node。pre 是第 m - 1 个 node
        """
        1 → 2 → 3 → 4 → 5 → 6
        我们要反转 2 → 3 → 4 → 5（m = 2, n = 5）

        reverse 是反转后的头指针：指向 5 → 4 → 3 → 2

        cur 是第 n+1 个节点，也就是 6

        pre 是第 m-1 个节点，也就是 1

        pre.next 是 2，但现在 2 的 next 是 None（因为它是 reverse 的尾）

        """
        # 把 reverse 后的最后一个 node 连接到原来 node 剩下的 right part
        pre.next.next = cur
        """
        pre 是 1

        pre.next 是 2（反转段的尾）

        所以 pre.next.next 是 2.next
        """
        # 把 reverse 后的 head node 连接到 m -1 的后面 pre.next = reverse
        pre.next = reverse

        return dummyNode.next

