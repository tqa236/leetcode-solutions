from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minimum = best_second = float("inf")
        for num in nums:
            if num <= minimum:
                minimum = num
            elif num <= best_second:
                best_second = num
            else:
                return True
        return False

    def increasingTripletNaive(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] < nums[j] and nums[j] < nums[k]:
                        return True
        return False