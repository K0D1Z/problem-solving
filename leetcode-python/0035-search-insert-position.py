class Solution:
    def searchInsert(self, nums, target) -> int:
        left = 0
        right = len(nums) - 1
        while right >= left:
            mid = (right + left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        if nums[mid] < target:
            return mid + 1
        return mid