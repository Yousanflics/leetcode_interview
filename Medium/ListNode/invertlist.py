class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    # iteration
    def reverseList(self, head: ListNode):
        prev = None
        current = head
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        return prev
    
    def reverseListRecursion(self, head):
        if not head or not head.next:
            return head
        new_head = self.reverseListRecursion(head.next)
        head.next.next = head
        head.next = None
        return new_head
    

def creat_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    # current = head
    # while current:
    #     print(f"{current.val}-> ", end="")
    #     # result.append(str(head.val))
    #     current = current.next
    # print()
    if not head:
        print()
        return
    result = []
    current = head
    while current:
        result.append(str(current.val))
        current = current.next
    print(" -> ".join(result))

if __name__ == '__main__':
    values = [1, 2, 3, 4, 5]
    head = creat_linked_list(values)
    print("Original List: ")
    print_linked_list(head)
    
    #test function
    solution = Solution()
    reverse_head = solution.reverseListRecursion(head)
    print("Reverse Recursively results: ")
    print_linked_list(reverse_head)

    
