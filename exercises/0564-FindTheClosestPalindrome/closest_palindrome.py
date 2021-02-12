def is_palindrome(n: str):
    return n == n[::-1]


def last_palindrome(first_half: str, center: str):
    if center and int(center) > 0:
        center = str(int(center) - 1)
    elif len(first_half) == len(str(int(first_half) - 1)) and int(first_half) > 1:
        first_half = str(int(first_half) - 1)
    else:
        if center:
            center = ""
            first_half = "9" * len(first_half)
        else:
            center = "9"
            first_half = "9" * (len(first_half) - 1)
    return first_half, center


def next_palindrome(first_half: str, center: str):
    if center and int(center) < 9:
        center = str(int(center) + 1)
    elif first_half and len(first_half) == len(str(int(first_half) + 1)):
        first_half = str(int(first_half) + 1)
    else:
        if center:
            center = ""
            first_half = "1" + "0" * (len(first_half))
        else:
            center = "0"
            first_half = "1" + "0" * (len(first_half) - 1)
    return first_half, center


def make_palindrome(first_half: str, center: str):
    return int(first_half + center + first_half[::-1])


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        num_digit = len(n)
        if num_digit % 2 == 0:
            center = ""
        else:
            center = n[num_digit // 2]
        first_half = n[: num_digit // 2]
        candidate = make_palindrome(first_half, center)
        candidates = [(first_half, center)]
        n = int(n)
        candidates.append(last_palindrome(first_half, center))
        candidates.append(next_palindrome(first_half, center))
        candidates = [make_palindrome(*candidate) for candidate in candidates]
        distance = float("inf")
        closest_candidate = None
        for candidate in candidates:
            if candidate == n:
                continue
            if abs(n - candidate) < distance or (
                abs(n - candidate) == distance and candidate < n
            ):
                distance = abs(n - candidate)
                closest_candidate = candidate
        return str(closest_candidate)
