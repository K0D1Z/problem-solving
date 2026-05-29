class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):
            return ""
        min_len = min([len(i) for i in strs])
        if not min_len:
            return ""
        prefix = ""
        for i in range(min_len):
            temp_prefix_letter = strs[0][i]
            for j in strs:
                if j[i] != temp_prefix_letter:
                    return prefix
            prefix += temp_prefix_letter
        return prefix
