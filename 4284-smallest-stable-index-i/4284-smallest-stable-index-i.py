class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return -1

        # suffix_min[i] = min(nums[i..n-1])
        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])

        # Running prefix max, checked in ascending order
        prefix_max = float("-inf")
        for i in range(n):
            prefix_max = max(prefix_max, nums[i])
            if prefix_max - suffix_min[i] <= k:
                return i

        return -1
        