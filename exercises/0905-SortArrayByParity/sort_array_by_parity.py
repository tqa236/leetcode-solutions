class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        return [i for i in nums if i % 2 == 0] + [i for i in nums if i % 2 == 1]
