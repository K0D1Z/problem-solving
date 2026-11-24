class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        d = dict()

        for nums in [nums1, nums2, nums3]:
            for n in set(nums):
                d[n] = 1 + d.get(n, 0)
        
        res = []
        for k, v in d.items():
            if v > 1:
                res.append(k)
        return res