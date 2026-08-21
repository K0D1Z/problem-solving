class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)
        res = ""
        for i in range(min(l1, l2)):
            res += word1[i] + word2[i]
        return res + (word1[l2:] if l1 > l2 else word2[l1:])
    