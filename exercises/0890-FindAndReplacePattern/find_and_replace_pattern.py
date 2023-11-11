from typing import List


def permutate_word(word, pattern):
    set_word = set(word)
    set_pair = set([(i, j) for i, j in zip(word, pattern)])
    return len(set_word) == len(set(pattern)) and len(set_word) == len(set_pair)


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        return [word for word in words if permutate_word(word, pattern)]
