class Solution:
    def countVowelStrings(self, n: int) -> int:
        num_vowel = 5
        partitions = [[1] * num_vowel for _ in range(n)]
        for i in range(1, n):
            for j in range(num_vowel):
                partitions[i][j] = sum(partitions[i - 1][: j + 1])
        return sum(partitions[-1])
