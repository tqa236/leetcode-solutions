from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        seq = {A[0]: {0: [0, 1, 1]}}
        for j in range(1, len(A)):
            if A[j] in seq:
                for key in seq[A[j]].keys():
                    if key != 0:
                        seq[A[j]][key][2] += 1
                seq[A[j]][0][0] += 1
                print("new", j, seq)
                continue
            seq[A[j]] = {0: [0, 1, 1]}
            for i in range(j):
                print("new", seq)
                print(i, j, A[i], A[j])
                diff = A[j] - A[i]
                print(i, j, A[j], diff, seq[A[j]])
                if diff in seq[A[j]]:
                    print("Aha")
                    seq[A[j]][diff][1] += 1
                    print(seq)
                elif diff in seq[A[i]]:
                    seq[A[j]][diff] = [
                        seq[A[i]][diff][0] + 1,
                        seq[A[i]][diff][1] * seq[A[i]][diff][2],
                        1,
                    ]
                    del seq[A[i]][diff]
                else:
                    seq[A[j]][diff] = [1, 1, 1]
        count = 0
        for key, val in seq.items():
            for diff, diff_count in val.items():
                if diff_count[0] >= 2:
                    count += (
                        ((diff_count[0] + 1) * (diff_count[0] - 2) // 2 + 1)
                        * diff_count[1]
                        * diff_count[2]
                    )
        return count
