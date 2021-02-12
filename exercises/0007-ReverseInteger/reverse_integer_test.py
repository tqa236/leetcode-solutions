import unittest

from reverse_integer import Solution


class Test(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.reverse(123), 321)


if __name__ == "__main__":
    unittest.main()
