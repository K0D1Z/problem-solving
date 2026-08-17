class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # STRAIGHTFORWARD SOLUTION
        # arr = [0,0,0]
        # for i in nums:
        #     arr[i] += 1
        # j = 0
        # for k in range(len(arr)):
        #     while arr[k] > 0:
        #         nums[j] = k
        #         arr[k] -= 1
        #         j += 1
        
        # ONE PASS PARTITION SOLUTION
        slow_ptr = 0
        fast_ptr = 0
        for val in range(3):            
            for _ in range(len(nums) - fast_ptr):
                if nums[fast_ptr] == val:
                    nums[slow_ptr], nums[fast_ptr] = nums[fast_ptr], nums[slow_ptr]
                    slow_ptr += 1
                fast_ptr += 1
            fast_ptr = slow_ptr

