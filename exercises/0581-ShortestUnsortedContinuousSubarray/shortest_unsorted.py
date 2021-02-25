from typing import List
import bisect


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        lowest = nums[0]
        highest = None
        curr_highest = None
        prev = None
        start = False
        start_index = None
        end_index = None
        for i, curr in enumerate(nums):
            if prev is None:
                prev = curr
                curr_highest = curr
                highest = curr
                continue
            if not start and curr < prev:
                start = True
                start_index = i - 1
                lowest = curr

            if curr < prev:
                end_index = i
                highest = curr_highest
            if curr < lowest:
                lowest = curr
            curr_highest = max(curr_highest, curr)
            if curr < highest:
                end_index = i
            prev = curr
        if not start:
            return 0
        start_index = bisect.bisect_right(nums[:start_index], lowest)
        return end_index - start_index + 1

    def findUnsortedSubarray2(self, nums: List[int]) -> int:
        start = -1
        end = -2
        min_val = nums[-1]
        max_val = nums[0]
        for i in range(1, len(nums)):
            max_val = max(max_val, nums[i])
            min_val = min(min_val, nums[-i - 1])
            if nums[i] < max_val:
                end = i
            if nums[-i - 1] > min_val:
                start = len(nums) - i - 1
        return end - start + 1

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