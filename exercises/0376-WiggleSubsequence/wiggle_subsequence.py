from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        curr_sub = []
        for i in range(len(nums)):
            if not curr_sub:
                curr_sub.append(nums[i])
            elif len(curr_sub) == 1:
                if nums[i] != curr_sub[-1]:
                    curr_sub.append(nums[i])
            elif curr_sub[-2] < curr_sub[-1]:
                if nums[i] < curr_sub[-1]:
                    curr_sub.append(nums[i])
                else:
                    curr_sub[-1] = nums[i]
            else:
                if nums[i] > curr_sub[-1]:
                    curr_sub.append(nums[i])
                else:
                    curr_sub[-1] = nums[i]
        return len(curr_sub)