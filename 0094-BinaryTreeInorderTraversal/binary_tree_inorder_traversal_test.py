import unittest

from binary_tree_inorder_traversal import TreeNode, Solution


class Test(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        root = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))
        self.assertEqual(solution.inorderTraversal(root), [1, 3, 2])

    def test_2(self):
        solution = Solution()
        self.assertEqual(solution.inorderTraversal(None), [])


if __name__ == "__main__":
    unittest.main()