from functools import reduce
from collections import Counter


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        return list(
            reduce(lambda x, y: x & y, [Counter(word) for word in words]).elements()
        )
