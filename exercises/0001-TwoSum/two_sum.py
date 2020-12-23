from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums1 = sorted(nums)
        i = 0
        j = len(nums1) - 1
        while True:
            value = nums1[i] + nums1[j]
            if value == target:
                if nums1[i] == nums1[j]:
                    return [
                        index for index, value in enumerate(nums) if value == nums1[i]
                    ]
                return [nums.index(nums1[i]), nums.index(nums1[j])]
            elif value < target:
                i = i + 1
            else:
                j = j - 1
