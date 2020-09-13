from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        newIntervals = []
        newIntervalStart = newInterval[0]
        newIntervalEnd = newInterval[1]
        start = False
        for index, interval in enumerate(intervals):
            if not start and interval[1] < newInterval[0]:
                newIntervals.append(interval)
                continue
            start = True
            if newIntervalEnd < interval[0]:
                newIntervals.append([newIntervalStart, newIntervalEnd])
                return newIntervals + intervals[index:]
            newIntervalStart = min(interval[0], newIntervalStart)
            newIntervalEnd = max(interval[1], newIntervalEnd)
        newIntervals.append([newIntervalStart, newIntervalEnd])
        return newIntervals
