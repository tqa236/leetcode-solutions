from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_counter = Counter(s)
        t_counter = Counter(t)
        for letter, count in t_counter.items():
            if letter not in s_counter or s_counter[letter] < count:
                return letter
