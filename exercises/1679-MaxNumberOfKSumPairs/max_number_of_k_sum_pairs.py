from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = {}
        count = 0
        for num in nums:
            if counter.get(num, 0) > 0:
                counter[num] = counter.get(num, 0) - 1
                count += 1
            else:
                counter[k - num] = counter.get(k - num, 0) + 1
        return count
