class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# 找出链表中环的起始节点，给定一个链表的head，如果链表中有环，则返回换的起始节点；如果没有环，则返回 null
# 最简单也是最直接的思路就是用 hash 集合记录已经访问的节点，如果是环的头那么肯定第一个二次访问，如果没有重复的那就直接返回  None 有的话那就是返回 head， 一遍遍历就可以完成，一遍遍历一遍加入到 set 中
# warning: 这里 python 里面的 set 在存对象的时候如果对象的地址不一样也是可以 add 的，即便 head.val 一样，因为内存地址不一样
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()

        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        return None
