import unittest

from shortest_unsorted import Solution


class Test(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]), 5)


if __name__ == "__main__":
    unittest.main()
