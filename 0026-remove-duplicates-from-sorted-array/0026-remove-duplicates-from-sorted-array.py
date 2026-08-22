class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # SECOND SOLUTION
        fast = 0
        slow = 0
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]   
            fast += 1
        return slow + 1
        
        # FIRST SOLUTION
        # i = 0
        # k = 0
        # while i < len(nums):
        #     curr = nums[i]
        #     while i+1 < len(nums):
        #         if nums[i+1] == curr:
        #             nums[i+1] = "_"
        #             i += 1
        #         else:
        #             break
        #     i += 1

        # slow = 0
        # fast = 0

        # while fast < len(nums):
        #     if nums[fast] != "_":
        #         nums[slow] = nums[fast]
        #         slow += 1
        #         k += 1
        #     fast += 1
        # return k
        