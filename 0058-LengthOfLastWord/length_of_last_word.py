class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        last_space = s.rfind(" ")
        if last_space == -1:
            return len(s)
        return len(s[last_space + 1 :])
