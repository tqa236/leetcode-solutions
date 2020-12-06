from collections import Counter
from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        player_dict = {1: "A", 0: "B"}
        last_player = len(moves) % 2
        last_player_moves = moves[1 - last_player :: 2]
        first_diagonal_win = all([[i, i] in last_player_moves for i in range(3)])
        second_diagonal_win = all([[i, 2 - i] in last_player_moves for i in range(3)])
        row_win = (
            Counter([move[0] for move in last_player_moves]).most_common(1)[0][1] >= 3
        )
        column_win = (
            Counter([move[1] for move in last_player_moves]).most_common(1)[0][1] >= 3
        )
        if any([first_diagonal_win, second_diagonal_win, row_win, column_win]):
            return player_dict[last_player]
        if len(moves) == 9:
            return "Draw"
        return "Pending"