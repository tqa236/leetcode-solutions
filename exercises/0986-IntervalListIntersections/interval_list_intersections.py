from typing import List


class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        intersection = []
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            list1 = firstList[i]
            list2 = secondList[j]
            overlap = [max(list1[0], list2[0]), min(list1[1], list2[1])]
            if overlap[0] <= overlap[1]:
                intersection.append(overlap)
            if list1[1] < list2[1]:
                i += 1
            elif list1 == list2[1]:
                i += 1
                j += 1
            else:
                j += 1
        return intersection
