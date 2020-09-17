class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        alt_remainder = 1 - n % 2
        while n != 0:
            remainder = n % 2
            if alt_remainder == remainder:
                return False
            n = n // 2
            alt_remainder = remainder
        return True