class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False


        hashmap = dict()
        for i in range(min(k + 1, len(nums))):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)
            if hashmap[nums[i]] == 2:
                return True
        
        for i in range(k + 1, len(nums)):
            hashmap[nums[i - k - 1]] -= 1
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)
            if hashmap[nums[i]] == 2:
                return True

        return False

        