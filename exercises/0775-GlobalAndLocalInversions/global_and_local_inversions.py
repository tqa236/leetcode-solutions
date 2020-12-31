from typing import List


class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        last_peak = float("-inf")
        for i in range(len(A) - 1):
            if A[i + 1] < last_peak:
                return False
            last_peak = max(A[i], last_peak)
        return True

    def isIdealPermutationNaive(self, A: List[int]) -> bool:
        for i, ai in enumerate(A[:-1]):
            for j, aj in enumerate(A[i + 1 :]):
                if ai > aj and j > 0:
                    return False
        return True