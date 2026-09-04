class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        reps = 0
        temp = nums[0]
        l = len(nums)

        if l == 1 or k == 0:
            return

        while reps < l:
            reps += 1
            idx = (i + k) % l
            c = nums[idx]
            nums[idx] = temp
            temp = c
            i = idx
            if k * reps % l == 0:
                i += 1
                temp = nums[i % l]