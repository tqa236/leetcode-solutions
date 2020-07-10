from itertools import combinations
from typing import Set, Tuple, List
from collections import Counter


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        count = Counter(nums)
        for key, value in count.most_common():
            if value >= 3:
                if key == 0:
                    result.append([0, 0, 0])
                    count[key] = 1
                else:
                    count[key] = 2
        nums = sorted(list(count.elements()))
        negative = [num for num in nums if num < 0]
        negative_set = set(negative)
        positive = [num for num in nums if num > 0]
        positive_set = set(positive)
        if 0 in nums:
            triplet_value = set([abs(num) for num in negative]).intersection(positive)
            for i in triplet_value:
                result.append([-i, 0, i])
        for first, second in set(combinations(negative, 2)):
            if abs(first + second) in positive_set:
                result.append(sorted([first, second, -first - second]))
        for first, second in set(combinations(positive, 2)):
            if (-first - second) in negative_set:
                result.append(sorted([first, second, -first - second]))
        return result
        return result + list(self.threeSumRecursion(nums))

    def threeSumRecursion(self, nums: List[int]) -> Set[Tuple[int]]:
        if len(nums) < 3:
            return set()
        if len(nums) == 3:
            if sum(nums) == 0:
                return set([(tuple(sorted(nums)))])
            return set()
        result = self.threeSumRecursion(nums[:-1])
        for i in set(combinations(nums[:-1], 2)):
            if sum(i) + nums[-1] == 0:
                result.add(tuple(sorted([i[0], i[1], nums[-1]])))
        return result
