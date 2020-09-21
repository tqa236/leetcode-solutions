class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        for char in palindrome[: len(palindrome) // 2]:
            if char != "a":
                return palindrome.replace(char, "a", 1)
        return palindrome[:-1] + "b"