class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # occurences = dict()
        # for i in nums:
        #     occurences[i] = 1 + occurences.get(i, 0)
        # freq = [[] for _ in range(len(nums) + 1)]

        # for j in occurences.keys():
        #     freq[occurences[j]].append(j)

        # res, idx = [], len(nums)
        # while k > 0:
        #     if freq[idx]:
        #         for i in freq[idx]:
        #             if k == 0:
        #                 return res
        #             res.append(i)
        #             k -= 1
        #     idx -= 1
        # return res

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        