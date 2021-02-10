class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        if not head:
            return None
        node = head
        new_node = None
        node_map = {}
        new_node_map = {}
        while node:
            if not new_node:
                new_node = Node(node.val, None, None)
                new_head = new_node
            new_node_map[node] = new_node
            if node.random in new_node_map:
                new_node.random = new_node_map[node.random]
            if node.random not in node_map:
                node_map[node.random] = [new_node]
            else:
                node_map[node.random].append(new_node)
            if node in node_map:
                for random_node in node_map[node]:
                    random_node.random = new_node
            node = node.next
            if node:
                new_node.next = Node(node.val, None, None)
            new_node = new_node.next
        return new_head
