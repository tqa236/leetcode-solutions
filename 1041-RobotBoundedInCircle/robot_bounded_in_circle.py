from typing import Tuple


class Robot:
    def __init__(self, position: Tuple[int, int], direction: Tuple[int, int]):
        self.position = position
        self.direction = direction
        self.directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    def move(self, action):
        if action == "G":
            self.position = tuple(a + b for a, b in zip(self.position, self.direction))
        else:
            rotate = {"L": 3, "R": 1}
            self.direction = self.directions[
                (self.directions.index(self.direction) + rotate[action]) % 4
            ]


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        robot = Robot((0, 0), (0, 1))
        for action in instructions:
            robot.move(action)
        return robot.position == (0, 0) or robot.direction != (0, 1)