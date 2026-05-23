import math


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [math.prod(nums[1:])]
        for i in range(len(nums) - 1):
            temp = result[i] * nums[i]
            if nums[i + 1] != 0:
                temp //= nums[i + 1]
            else:
                temp = math.prod(nums[:i + 1])
                temp *= math.prod(nums[i + 2:])
            result.append(temp)
        return result
