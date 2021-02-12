import unittest

from majority_element_ii import Solution


class Test(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.majorityElement([3, 2, 3]), [3])


if __name__ == "__main__":
    unittest.main()
