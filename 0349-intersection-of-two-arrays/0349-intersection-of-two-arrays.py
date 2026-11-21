class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hashmap1 = set(nums1)
        hashmap2 = set(nums2)

        return list(hashmap1.intersection(hashmap2))
        
        