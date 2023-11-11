from utils.linked_list import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = prev = ListNode(0)
        prev.next = head
        while prev.next and prev.next.next:
            a = prev.next
            b = prev.next.next
            c = prev.next.next.next
            prev.next = b
            prev.next.next = a
            prev.next.next.next = c
            prev = prev.next.next
        return dummy.next
