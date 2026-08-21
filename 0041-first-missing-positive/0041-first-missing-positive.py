class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        smallest = 1
        maximum = len(nums) + 1
        nums = set(nums)
        while smallest in nums and smallest < maximum:
            smallest += 1
        return smallest
        