import bisect
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key=lambda x: (x[1], x[2]))
        capacity_left = capacity
        passengers = {}
        get_offs = []
        for trip in trips:
            capacity_left -= trip[0]
            if trip[2] not in get_offs:
                bisect.insort(get_offs, trip[2])
            while get_offs[0] <= trip[1]:
                capacity_left += passengers[get_offs.pop(0)]
            passengers[trip[2]] = passengers.get(trip[2], 0) + trip[0]
            if capacity_left < 0:
                return False
        return True
