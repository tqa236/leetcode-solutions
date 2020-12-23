class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters_rev = [char for char in S[::-1] if char.isalpha()]
        S_rev = []
        j = 0
        for char in S:
            if char.isalpha():
                S_rev.append(letters_rev[j])
                j += 1
            else:
                S_rev.append(char)
        return "".join(S_rev)