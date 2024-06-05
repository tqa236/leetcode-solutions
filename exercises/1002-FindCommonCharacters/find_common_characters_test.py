import unittest
from find_common_characters import Solution


class Test(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        self.assertEqual(
            set(solution.commonChars(["bella", "label", "roller"])),
            set(["e", "l", "l"]),
        )



if __name__ == "__main__":
    unittest.main()