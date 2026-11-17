class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        h = dict()
        r = []
        for n in nums1:
            h[n] = 1 + h.get(n, 0)
        for n in nums2:
            if h.get(n, 0) > 0:
                r.append(n)
                h[n] -= 1
        return r

        