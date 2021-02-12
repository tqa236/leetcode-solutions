class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        chars = set()
        index = 0
        for c in s:
            if c not in chars:
                chars.add(c)
            else:
                max_length = max(max_length, len(chars))
                while s[index] != c:
                    chars.discard(s[index])
                    index += 1
                index += 1
        return max(max_length, len(chars))
