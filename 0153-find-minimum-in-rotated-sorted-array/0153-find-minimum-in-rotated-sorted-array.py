class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 1
        r = len(nums) - 1
        minimum = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                minimum = min(nums[l], minimum)
                break

            m = (l + r) // 2
            minimum = min(nums[m], minimum)
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return minimum
        