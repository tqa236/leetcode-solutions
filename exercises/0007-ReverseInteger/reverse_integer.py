class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        x = sign * int(str(abs(x))[::-1])
        if -(2 ** 31) <= x <= 2 ** 31 - 1:
            return x
        return 0