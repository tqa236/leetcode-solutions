import unittest

from tree import make_tree


class Test(unittest.TestCase):
    def test_1(self):
        values = [3, 9, 20, None, None, 15, 7]
        root = make_tree(values)
        self.assertEqual(root.val, 3)
        self.assertEqual(root.left.val, 9)
        self.assertEqual(root.right.val, 20)
        self.assertEqual(root.left.left, None)
        self.assertEqual(root.left.right, None)
        self.assertEqual(root.right.left.val, 15)
        self.assertEqual(root.right.right.val, 7)


if __name__ == "__main__":
    unittest.main()
