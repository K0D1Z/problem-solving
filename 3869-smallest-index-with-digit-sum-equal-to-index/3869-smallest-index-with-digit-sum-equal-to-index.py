class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            temp = 0
            for j in str(nums[i]):
                temp += int(j)
            if temp == i:
                return temp
        return -1
        