from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # 2 <= rows, cols <= 70
        rows = len(grid)
        cols = len(grid[0])
        last_positions = set([(0, 0, cols - 1)])
        cherries = {(0, 0, cols - 1): grid[0][0] + grid[0][cols - 1]}
        for row in range(1, rows):
            positions = []
            for last_position in last_positions:
                new_pos1 = range(
                    max(0, last_position[1] - 1), min(cols, last_position[1] + 2)
                )
                new_pos2 = range(
                    max(0, last_position[2] - 1), min(cols, last_position[2] + 2)
                )
                for pos1 in new_pos1:
                    for pos2 in new_pos2:
                        if pos1 == pos2:
                            cherry = grid[row][pos1]
                        else:
                            cherry = grid[row][pos1] + grid[row][pos2]
                        position = (row, pos1, pos2)
                        positions.append(position)
                        cherries[position] = max(
                            cherries.get(position, 0),
                            cherries[last_position] + cherry,
                        )
            last_positions = set(positions)
        return max([cherries[key] for key in last_positions])
