from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        remain = []
        for bit in bits[-2::-1]:
            if not remain:
                if bit == 0:
                    return True
                else:
                    remain.append(bit)
            elif remain == [1]:
                if bit == 1:
                    remain = []
                else:
                    return False
        return not remain