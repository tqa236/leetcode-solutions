from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        counter = 0
        product = 1
        subarray = []
        last_count = 0
        for num in nums:
            subarray.append(num)
            product *= num
            if product >= k:
                counter -= last_count
                counter += len(subarray) * (len(subarray) - 1) // 2
                while product >= k and subarray:
                    out = subarray.pop(0)
                    product /= out
                last_count = len(subarray) * (len(subarray) - 1) // 2
        counter -= last_count
        counter += len(subarray) * (len(subarray) + 1) // 2
        return counter