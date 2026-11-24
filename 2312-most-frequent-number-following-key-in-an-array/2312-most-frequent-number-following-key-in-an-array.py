class Solution:
    def mostFrequent(self, nums: list[int], key: int) -> int:
        d = dict()
        for i in range(len(nums) - 1):
            if nums[i] == key:
                d[nums[i+1]] = 1 + d.get(nums[i+1], 0)
        
        m = max(d.items(), key = lambda x: x[1])
        return m[0]
        