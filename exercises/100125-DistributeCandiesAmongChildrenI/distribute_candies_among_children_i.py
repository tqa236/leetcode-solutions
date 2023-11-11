from math import comb


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        k = 3
        general_case = comb(n + k - 1, 2)
        one_limit = (
            comb(n + k - 1 - (limit + 1), 2) if n + k - 1 - (limit + 1) >= 0 else 0
        )
        two_limit = (
            comb(n + k - 1 - 2 * (limit + 1), 2)
            if n + k - 1 - 2 * (limit + 1) >= 0
            else 0
        )
        three_limit = (
            comb(n + k - 1 - 3 * (limit + 1), 2)
            if n + k - 1 - 3 * (limit + 1) >= 0
            else 0
        )
        result = general_case - 3 * one_limit + 3 * two_limit - three_limit
        return result
