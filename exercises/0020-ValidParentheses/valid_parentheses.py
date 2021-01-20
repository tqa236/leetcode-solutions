class Solution:
    def isValid(self, s: str) -> bool:
        left = []
        matches = {")": "(", "]": "[", "}": "{"}
        for i in s:
            if i in "([{":
                left.append(i)
            else:
                if not left:
                    return False
                parenthese = left.pop()
                if matches[i] != parenthese:
                    return False
        return not left