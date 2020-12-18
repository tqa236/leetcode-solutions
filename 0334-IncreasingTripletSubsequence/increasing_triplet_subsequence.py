from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        true_minimum = nums[0]
        best_local_second = true_second = None
        for num in nums[1:]:
            if num < true_minimum:
                if true_second is not None:
                    best_local_second = true_second
                true_minimum = num
                true_second = None
            elif num > true_minimum:
                if true_second is None:
                    if best_local_second is not None and num > best_local_second:
                        return True
                    true_second = num
                else:
                    if num < true_second:
                        true_second = num
                    elif num > true_second:
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