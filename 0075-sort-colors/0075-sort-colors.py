class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # STRAIGHTFORWARD SOLUTION
        arr = [0,0,0]
        for i in nums:
            arr[i] += 1
        j = 0
        for k in range(len(arr)):
            while arr[k] > 0:
                nums[j] = k
                arr[k] -= 1
                j += 1
        
        