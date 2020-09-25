from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        max_len = len(str(max(nums))) * 2
        return (
            "".join(
                sorted(
                    [str(i) for i in nums],
                    key=lambda num: (num * (max_len // len(num) + 1))[:max_len],
                    reverse=True,
                )
            ).lstrip("0")
            or "0"
        )
