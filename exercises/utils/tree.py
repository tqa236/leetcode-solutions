from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_tree(values: List[int]):
    """Make a tree from a list using BFS."""
    if not values:
        return None
    root = TreeNode(values[0], None, None)
    queue = [root]
    for index, value in enumerate(values[1:]):
        node = queue[0]
        if index % 2 == 0:
            if value is not None:
                node.left = TreeNode(value, None, None)
                queue.append(node.left)
        else:
            if value is not None:
                node.right = TreeNode(value, None, None)
                queue.append(node.right)
            queue.pop(0)
    return root
