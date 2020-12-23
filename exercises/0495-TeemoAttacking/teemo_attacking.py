from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        return (
            sum(
                min(timeSeries[i] - timeSeries[i - 1], duration)
                for i in range(1, len(timeSeries))
            )
            + duration
        )
