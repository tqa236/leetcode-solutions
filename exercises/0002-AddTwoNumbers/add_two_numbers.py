class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        memory = 0
        head = None
        while l1 or l2:
            value = memory
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            if value >= 10:
                value -= 10
                memory = 1
            else:
                memory = 0
            if not head:
                head = ListNode(value, None)
                node = head
            else:
                node.next = ListNode(value, None)
                node = node.next
        if memory == 1:
            node.next = ListNode(memory, None)
        return head
