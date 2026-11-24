class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        d = dict()
        for n in nums:
            d[n] = 1 + d.get(n, 0)
        
        for v in d.values():
            if v % 2 != 0:
                return False
        return True