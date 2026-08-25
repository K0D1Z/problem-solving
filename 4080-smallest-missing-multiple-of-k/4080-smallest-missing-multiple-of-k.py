class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        hashset = set()
        for i in nums:
            if i % k == 0:
                hashset.add(i)
        n = k
        for _ in range(len(hashset)):
            if n not in hashset:
                return n
            n += k
        return n