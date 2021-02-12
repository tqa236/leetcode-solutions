class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = {}
        char_map_reverse = {}
        for char_s, char_t in zip(s, t):
            if char_s not in char_map and char_t not in char_map_reverse:
                char_map[char_s] = char_t
                char_map_reverse[char_t] = char_s
            if (
                char_map.get(char_s, None) != char_t
                or char_map_reverse.get(char_t, None) != char_s
            ):
                return False
        return True
