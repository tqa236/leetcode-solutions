from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        num_digits_low = len(str(low))
        num_digits_high = len(str(high))
        sequential_digits = []
        for i in range(num_digits_low, num_digits_high + 1):
            for digit in range(1, 11 - i):
                number = int("".join([str(digit + index) for index in range(i)]))
                if low <= number <= high:
                    sequential_digits.append(number)
        return sequential_digits
