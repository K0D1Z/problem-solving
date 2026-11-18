class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        res = 0
        temp_res = 0
        for n in nums:
            if n == 0:
                res = max(res, temp_res)
                temp_res = 0
            else:
                temp_res += 1
        return max(res, temp_res)