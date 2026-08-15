class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 1. EASIEST SOLUTION - SORT AND GET N/2 ELEMENT - BUT IT IS SLOW
        # return sorted(nums)[len(nums) // 2]

        # 2. ALTERNATIVELY - USE HASHMAP
        # hashmap = {}
        # for i in nums:
        #     hashmap[i] = 1 + hashmap.get(i, 0)
        # maximum = max(hashmap.items(), key=lambda x: x[1])
        # return maximum[0]

        # 3. OPTIMAL (BOYER-MOORE) - IT WORKS BECAUSE IT IS GUARANTEED THAT MAJORITY ELEMENT EXISTS
        count = 1
        result = nums[0]

        for n in nums[1:]:
            if n == result:
                count += 1
            elif count <= 0:
                count = 1
                result = n
            else:
                count -= 1
        return result

        # 4. NEETCODE SOLUTION
        # res, count = 0, 0
        # for n in nums:
        #     if count == 0 res = n
        #     count += (1 if n == res else -1)
        # return result
