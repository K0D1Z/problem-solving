class Solution:
    def search(self, nums: list[int], target: int) -> int:

        def binary_search(l, r):
            while l <= r:
                m = (l+r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return -1

        l, r = 0, len(nums) - 1
        minimum = float('inf')
        rotation_idx = 0

        # IF ARRAY IS ALREADY IN SORTED ORDER: JUST DO ORDINARY BINARY SEARCH
        if nums[l] < nums[r]:
            return binary_search(l, r)

        # ELSE: FIND ROTATION INDEX
        while l <= r:
            if nums[l] < nums[r]:
                if minimum > nums[l]:
                    minimum = nums[l]
                    rotation_idx = l
                break
                
            m = (l + r) // 2
            
            if minimum > nums[m]:
                minimum = nums[m]
                rotation_idx = m

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
                    
        # SELECT PART OF THE ARRAY TO PERFORM BINARY SEARCH ON
        if nums[max(rotation_idx - 1, 0)] >= target >= nums[0]:
            l = 0
            r = max(rotation_idx - 1, 0)
        else:
            l = rotation_idx
            r = len(nums) - 1
        
        # ORDINARY BINARY SEARCH
        return binary_search(l, r)
