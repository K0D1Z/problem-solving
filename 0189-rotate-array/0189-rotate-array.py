class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # FIRST APPROACH
        
        # i = 0
        # reps = 0
        # temp = nums[0]
        # l = len(nums)

        # if l == 1 or k == 0:
        #     return

        # while reps < l:
        #     reps += 1
        #     idx = (i + k) % l
        #     c = nums[idx]
        #     nums[idx] = temp
        #     temp = c
        #     i = idx
        #     if k * reps % l == 0:
        #         i += 1
        #         temp = nums[i % l]

        # OPTIMAL APPROACH

        k %= len(nums)

        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1


        


