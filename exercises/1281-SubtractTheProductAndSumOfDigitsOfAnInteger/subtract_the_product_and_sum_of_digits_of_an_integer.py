import math


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(i) for i in str(n)]
        return math.prod(digits) - sum(digits)
