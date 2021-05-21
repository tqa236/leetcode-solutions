from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Divide the array to subarray by zero.
        There can be maximum 1 negative number that can divide the subarray.
        """
        max_prod = None
        curr_prod = None
        curr_neg = None
        max_pos = None
        max_all = None
        preprod = []
        for num in nums:
            if num == 0:
                max_prod = max(max_prod, curr_prod)
            elif num > 0 and not max_pos:
                pass
            #     max_pos = num
            #     max_all = num
            # elif num < 0 and not max_all:
            #     max_all = num
            # elif num > 0:
