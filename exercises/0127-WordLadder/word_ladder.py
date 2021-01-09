import string
from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        candidates = deque([[beginWord, 1]])
        while candidates:
            candidate, distance = candidates.popleft()
            if candidate == endWord:
                return distance
            for i in range(len(candidate)):
                for c in string.ascii_lowercase:
                    new_candidate = candidate[:i] + c + candidate[i + 1 :]
                    if new_candidate in wordList:
                        wordList.remove(new_candidate)
                        candidates.append([new_candidate, distance + 1])
        return 0