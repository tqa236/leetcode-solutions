import unittest
from kth_largest_element_in_an_array import Solution


class Test(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2), 5)


if __name__ == "__main__":
    unittest.main()
