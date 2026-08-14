class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        l = min(list(map(lambda x: len(x), strs)))
        for i in range(l):
            for s in strs:
                if s[i] != strs[0][i]:
                    return result
            result += s[i]
        return result