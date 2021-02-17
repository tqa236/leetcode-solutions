from typing import List


def find_neighbor(cell, N):
    neighbors = set(
        [
            (i, j)
            for i in range(max(0, cell[0] - 1), min(N, cell[0] + 2))
            for j in range(max(0, cell[1] - 1), min(N, cell[1] + 2))
        ]
    )
    neighbors.remove(cell)
    return neighbors


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        if len(grid) == 1:
            return 1
        visited = set()
        to_visit = [(0, 0)]
        length = {(0, 0): 1}
        end = (len(grid) - 1, len(grid) - 1)
        while to_visit:
            start = to_visit.pop(0)
            visited.add(start)
            neighbors = find_neighbor(start, len(grid))
            for neighbor in neighbors:
                if neighbor == end:
                    return length[start] + 1
                if grid[neighbor[0]][neighbor[1]] == 1:
                    visited.add(neighbor)
                elif neighbor not in visited and neighbor not in to_visit:
                    length[neighbor] = length[start] + 1
                    to_visit.append(neighbor)
        return -1