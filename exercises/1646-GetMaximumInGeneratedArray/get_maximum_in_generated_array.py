class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        array = [0, 1]
        max_value = 1
        for i in range(2, n + 1):
            if i % 2 == 0:
                value = array[i // 2]
            else:
                value = array[i // 2] + array[i // 2 + 1]
            max_value = max(max_value, value)
            array.append(value)
        return max_value
