class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # OPTIMAL
        l, total = 0, 0
        res = float('inf')

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1

        return 0 if res == float('inf') else res


        # FIRST ATTEMPT

        # result = 0
        # l, r = 0, 0
        
        # while target > 0 and r < len(nums):
        #     target -= nums[r]
        #     r += 1
            
        # if r == len(nums) and target > 0:
        #     return 0

        # result = r - l

        # while r < len(nums):
        #     target -= nums[r]
        #     r += 1
        #     while target + nums[l] <= 0:
        #         target += nums[l]
        #         l += 1
        #     result = min(result, r - l)
        
        # while target + nums[l] <= 0:
        #     target += nums[l]
        #     l += 1
        # result = min(result, r - l)

        # return result
        