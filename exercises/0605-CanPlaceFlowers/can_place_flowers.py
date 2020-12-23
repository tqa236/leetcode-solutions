from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        is_empty = True
        is_adjacent = False
        num_flower = 0
        for i in range(len(flowerbed) - 1):
            if flowerbed[i] == 0:
                if is_empty:
                    is_adjacent = False or flowerbed[i + 1] == 1
                is_empty = True
            else:
                is_empty = False
                is_adjacent = True
            if is_empty and not is_adjacent:
                num_flower += 1
                is_empty = False
                is_adjacent = True
        if flowerbed[-1] == 0 and is_empty:
            num_flower += 1
        return n <= num_flower
