import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        return n == 4 ** int(round(math.log(n, 4)))
