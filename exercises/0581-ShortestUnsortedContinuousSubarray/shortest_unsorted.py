from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
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
