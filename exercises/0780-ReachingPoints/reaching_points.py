import queue


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        start = (sx, sy)
        goal = (tx, ty)
        if start == goal:
            return True
        while goal[0] > start[0] and goal[1] > start[1]:
            if goal[0] > goal[1]:
                goal = (
                    goal[0] - ((goal[0] - goal[1]) // goal[1] + 1) * goal[1],
                    goal[1],
                )
            else:
                goal = (
                    goal[0],
                    goal[1] - ((goal[1] - goal[0]) // goal[0] + 1) * goal[0],
                )
        if goal[0] == start[0]:
            return goal[1] >= start[1] and (goal[1] - start[1]) % goal[0] == 0
        elif goal[1] == start[1]:
            return goal[0] >= start[0] and (goal[0] - start[0]) % goal[1] == 0
        return False

    def reachingPointsNaive(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        start = (sx, sy)
        goal = (tx, ty)
        if start == goal:
            return True
        q = queue.Queue()
        q.put(start)
        while not q.empty():
            point = q.get()
            left = (point[0] + point[1], point[1])
            right = (point[0], point[0] + point[1])
            if goal in (left, right):
                return True
            for new_point in [left, right]:
                if goal[0] >= new_point[0] and goal[1] >= new_point[1]:
                    q.put(new_point)
        return False
