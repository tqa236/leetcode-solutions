from utils.tree import TreeNode


def height(node):
    if node is None:
        return 0
    return max(height(node.left), height(node.right)) + 1


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False
        lh = height(root.left)
        rh = height(root.right)
        return abs(lh - rh) <= 1
