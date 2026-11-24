class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m = max(nums)
        if len(nums) > m + 1:
            return False

        d = dict()
        for n in nums:
            d[n] = 1 + d.get(n, 0)
        
        if d.get(m, 0) != 2:
            return False
        
        for i in range(1, m):
            if d.get(i, 0) != 1:
                return False
        return True
        