from typing import List
from collections import Counter


class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        counter = Counter(words)
        print(counter)
        return sum(counter[word] for word in counter if self.checkSubsequence(S, word))

    @staticmethod
    def checkSubsequence(S: str, word: str) -> bool:
        i = 0
        for char in S:
            if word[i] == char:
                i += 1
            if i == len(word):
                return True
        return False