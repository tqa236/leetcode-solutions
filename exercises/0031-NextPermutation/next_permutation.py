from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        index_i = -1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                index_i = i
        if index_i < 0:
            nums.reverse()
            return
        for j in range(index_i + 1, len(nums)):
            if nums[j] > nums[index_i]:
                index_j = j
        nums[index_i], nums[index_j] = nums[index_j], nums[index_i]
        nums[index_i + 1 :] = nums[index_i + 1 :][::-1]
        return
