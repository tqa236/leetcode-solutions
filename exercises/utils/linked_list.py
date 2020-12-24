class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def make_linked_list(values):
    if not values:
        return None
    last_node = None
    for value in values:
        node = ListNode(value)
        if last_node:
            last_node.next = node
        else:
            head = node
        last_node = node
    return head


def linked_list_to_list(head):
    node = head
    values = []
    while node:
        values.append(node.val)
        node = node.next
    return values