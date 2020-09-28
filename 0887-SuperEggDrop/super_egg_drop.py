class Solution(object):
    def superEggDrop(self, K: int, N: int) -> int:
        print(K, N)
        print((N + 1) // 2 ** (2 - 1) + 2 - 1)
        drops = []
        for k in range(K):
            if k == 0:
                drops.append(N)
            if k > 0:
                drops.append((N + 1) // 2 ** k + k)
            print(k, drops)
        # drops = [(N + 1) // 2 ** (k - 1) + k - 1 if k > 0 else N for k in range(K)]
        print(drops)
        return min(drops)
