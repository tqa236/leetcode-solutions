import unittest
from subtract_the_product_and_sum_of_digits_of_an_integer import Solution


class Test(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.subtractProductAndSum(234), 15)


if __name__ == "__main__":
    unittest.main()