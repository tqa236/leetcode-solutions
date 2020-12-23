from typing import List


from utils.tree import TreeNode


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
