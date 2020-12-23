class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        different_pairs = {"xy": 0, "yx": 0}
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                different_pairs[c1 + c2] += 1
        if (different_pairs["xy"] + different_pairs["yx"]) % 2 != 0:
            return -1
        return (
            different_pairs["xy"] // 2
            + different_pairs["yx"] // 2
            + 2 * (different_pairs["xy"] % 2)
        )
