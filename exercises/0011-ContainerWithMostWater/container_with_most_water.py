from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_value = 0
        while i < j:
            base = min(height[i], height[j])
            max_value = max(max_value, base * (j - i))
            while height[i] <= base and i < j:
                i += 1
            while height[j] <= base and i < j:
                j -= 1
        return max_value

    def maxAreaNaive(self, height: List[int]) -> int:
        return max(
            [
                min(height[i], height[j]) * (j - i)
                for i in range(len(height))
                for j in range(i + 1, len(height))
            ]
        )