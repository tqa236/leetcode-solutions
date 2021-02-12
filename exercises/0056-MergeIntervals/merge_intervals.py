from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        merged_intervals = [intervals[0]]
        for interval in intervals[1:]:
            if merged_intervals[-1][1] >= interval[0]:
                merged_intervals[-1][1] = max(interval[1], merged_intervals[-1][1])
            else:
                merged_intervals.append(interval)
        return merged_intervals
