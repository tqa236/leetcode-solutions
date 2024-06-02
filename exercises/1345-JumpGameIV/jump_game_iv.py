from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        min_jump = [10**9] * len(arr)
        min_jump[0] = 0
        queue = [0]
        value_index_dict = {}
        min_jump_node = 0
        visited = set()
        for index, value in enumerate(arr):
            if value not in value_index_dict:
                value_index_dict[value] = []
            value_index_dict[value].append(index)
        while queue:
            node = queue.pop(0)
            distance = min_jump_node
            min_jump_node = min_jump[node]
            if distance + 1 <= min_jump[-1] < 10**9:
                return min_jump[-1]
            if node > 0 and min_jump[node - 1] > min_jump_node + 1:
                min_jump[node - 1] = min_jump_node + 1
                queue.append(node - 1)
            if node < len(arr) - 1 and min_jump[node + 1] > min_jump_node + 1:
                min_jump[node + 1] = min_jump_node + 1
                queue.append(node + 1)
            if arr[node] not in visited:
                for index in value_index_dict[arr[node]][::-1]:
                    if index != node and min_jump[index] > min_jump_node + 1:
                        min_jump[index] = min_jump_node + 1
                        queue.append(index)
                visited.add(arr[node])
        return min_jump[-1]
