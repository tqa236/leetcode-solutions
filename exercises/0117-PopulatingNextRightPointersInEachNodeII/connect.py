class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        dummy = tail = Node(0)
        node = root
        while node:
            for c in (node.left, node.right):
                tail.next = c
                if c:
                    tail = tail.next
            if node.next:
                node = node.next
            else:
                node, tail = dummy.next, dummy
        return root
