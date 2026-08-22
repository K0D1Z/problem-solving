class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if not m:
            nums1[:] = nums2.copy()
            return
        if not n:
            return

        length = n + m
        n, m = n - 1, m - 1
        

        for i in range(length - 1, -1, -1):
            if n == -1:
                break
            elif m == -1:
                nums1[:i+1] = nums2[:n+1]
                break
            
            if nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
                        