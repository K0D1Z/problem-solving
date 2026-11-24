class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        res = []
        
        s1 = set(nums1)
        s2 = set(nums2)

        i = s1.intersection(s2)

        s1 -= i
        s2 -= i

        res.append(list(s1))
        res.append(list(s2))

        return res
