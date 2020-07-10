import math


class Solution(object):
    def __init__(self):
        self.ugly_numbers = [1, 2, 3, 4, 5]
        self.start = 0

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= len(self.ugly_numbers):
            return self.ugly_numbers[n - 1]
        while n > len(self.ugly_numbers):
            max_ugly_number = self.ugly_numbers[-1]
            while True:
                if self.ugly_numbers[self.start] * 5 <= max_ugly_number:
                    self.start += 1
                else:
                    break
            upperbound = int(math.floor(math.log(max_ugly_number, 2)))
            upperbound_index = self.ugly_numbers.index(2 ** upperbound) + 2
            candidates = [
                ugly_number * factor
                for ugly_number in self.ugly_numbers[self.start : upperbound_index]
                for factor in [2, 3, 5]
                if ugly_number * factor > max_ugly_number
            ]
            self.ugly_numbers.append(min(candidates))
        return self.ugly_numbers[n - 1]
