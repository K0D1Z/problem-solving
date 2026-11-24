class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        d = dict()
        for n in nums:
            d[n] = 1 + d.get(n, 0)
        res = 0
        for k, v in d.items():
            if v == 1:
                res += k
        return res