from typing import List
import bisect


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        prev = None
        start = False
        start_index = None
        end_index = None
        for i, curr in enumerate(nums):
            if prev is None:
                lowest = prev = curr_highest = highest = curr
                continue
            if not start and curr < prev:
                start = True
                start_index = i - 1
                lowest = curr
            if curr < prev:
                highest = curr_highest
            lowest = min(curr, lowest)
            curr_highest = max(curr_highest, curr)
            if curr < highest:
                end_index = i
            prev = curr
        if not start:
            return 0
        start_index = bisect.bisect_right(nums[:start_index], lowest)
        return end_index - start_index + 1

    def findUnsortedSubarrayNaive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        start = -1
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                start = i
                break
        if start == -1:
            return 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != sorted_nums[i]:
                stop = i
                break
        return stop - start + 1