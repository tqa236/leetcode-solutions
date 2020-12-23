from collections import Counter
from typing import List


class Solution(object):
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) // 3
        counter = Counter(nums)
        return [
            element for element, count in counter.most_common() if count > threshold
        ]
