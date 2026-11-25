class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        first_greatest = float('-inf')
        second_greatest = float('-inf')
        first_idx = None

        for n in range(len(nums)):
            if nums[n] > first_greatest:
                second_greatest = max(second_greatest, first_greatest)
                first_greatest = nums[n]
                first_idx = n
            if nums[n] > second_greatest and first_idx != n:
                second_greatest = nums[n]
        
        return (first_greatest - 1) * (second_greatest - 1)
