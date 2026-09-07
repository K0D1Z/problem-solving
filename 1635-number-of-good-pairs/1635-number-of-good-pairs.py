class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = dict()
        result = 0
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        
        for k in freq:
            n = freq[k]
            result += (n * (n - 1)) // 2

        return result


        