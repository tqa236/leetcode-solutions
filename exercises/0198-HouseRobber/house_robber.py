from typing import List


class Solution:
    def __init__(self):
        self.max_amount = []

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= len(self.max_amount):
            return self.max_amount[len(nums) - 1]
        if len(nums) == 1:
            self.max_amount.append(nums[0])
            return nums[0]
        max_amount = max(nums[-1] + self.rob(nums[:-2]), self.rob(nums[:-1]))
        self.max_amount.append(max_amount)
        return max_amount
