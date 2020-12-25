from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        rows = len(matrix)
        columns = len(matrix[0])
        i = j = 0
        diagonal_order = []
        up = True
        while i <= rows - 1 and j <= columns - 1:
            diagonal_order.append(matrix[i][j])
            if (i == 0 or j == columns - 1) and up:
                up = False
                if j == columns - 1:
                    i += 1
                else:
                    j += 1
            elif (i == rows - 1 or j == 0) and not up:
                up = True
                if i == rows - 1:
                    j += 1
                else:
                    i += 1
            elif up:
                i -= 1
                j += 1
            else:
                i += 1
                j -= 1
        return diagonal_order
