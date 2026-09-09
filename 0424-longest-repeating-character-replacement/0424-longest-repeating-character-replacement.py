class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # FIRST IDEA (NON OPTIMAL O(N*M) WHERE M=26)

        # freq = dict()
        # l, r = 0, 0
        # res = 0
        # while r < len(s):
        #     freq[s[r]] = 1 + freq.get(s[r], 0)
        #     freq_max = max(freq.values())
        #     if r - l + 1 - freq_max <= k:
        #         res = max(res, r - l + 1)
        #     else:
        #         while r - l + 1 - freq_max > k:
        #             freq[s[l]] -= 1
        #             l += 1
        #             freq_max = max(freq.values())
        #     r += 1
        # return res

        # OPTIMAL (freq_max should not change)

        count = dict()
        res = 0
        l = 0
        max_f = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_f = max(max_f, count[s[r]])

            while (r - l + 1) - max_f > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res