class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: 1} # starting prefix count - edgecase
        prefix = 0
        result = 0
        for n in nums:
            prefix += n
            result += prefix_sum.get((prefix - k), 0)
            prefix_sum[prefix] = 1 + prefix_sum.get(prefix, 0)
        return result