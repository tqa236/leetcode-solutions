from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        traversal = []
        if root is not None:
            if root.left:
                traversal += self.inorderTraversal(root.left)
            traversal.append(root.val)
            if root.right:
                traversal += self.inorderTraversal(root.right)
        return traversal
