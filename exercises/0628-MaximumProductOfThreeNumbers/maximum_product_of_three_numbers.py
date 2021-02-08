from typing import List
import heapq


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(a[0] * a[1] * a[2], b[0] * b[1] * a[0])

    def maximumProductNaive(self, nums: List[int]) -> int:
        max_num = float("-inf")
        num_len = len(nums)
        for i in range(num_len):
            for j in range(i + 1, num_len):
                for k in range(j + 1, num_len):
                    max_num = max(max_num, nums[i] * nums[j] * nums[k])
        return max_num