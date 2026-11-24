class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        d = set()
        for i in nums:
            if i in d:
                return i
            d.add(i)