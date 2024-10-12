def find_common_prefix(str1: str, str2: str):
    common_prefix = ""
    for x, y in zip(str1, str2):
        if x == y:
            common_prefix += x
        else:
            break
    return common_prefix


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common_prefix = strs[0]
        for str_ in strs[1:]:
            common_prefix = find_common_prefix(common_prefix, str_)
        return common_prefix
