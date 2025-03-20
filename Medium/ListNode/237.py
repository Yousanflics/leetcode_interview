# Definition for singly-linked list

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        # node.val = node.next.val
        # node.next = node.next.next
        # 这种可以解决但是可以更快，就是将 node.next 缓存起来
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next
