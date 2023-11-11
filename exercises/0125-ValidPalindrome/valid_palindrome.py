class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_characters = [char.lower() for char in s if char.isalnum()]
        return cleaned_characters == cleaned_characters[::-1]
