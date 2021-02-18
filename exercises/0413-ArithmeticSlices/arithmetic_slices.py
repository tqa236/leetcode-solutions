from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        diff = None
        diff_count = 0
        count = 0
        for i in range(len(A) - 1):
            if A[i + 1] - A[i] != diff:
                if diff_count >= 2:
                    count += (diff_count + 1) * (diff_count - 2) // 2 + 1
                diff = A[i + 1] - A[i]
                diff_count = 1
            else:
                diff_count += 1
        if diff_count >= 2:
            count += (diff_count + 1) * (diff_count - 2) // 2 + 1
        return count