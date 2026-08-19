class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # MY SOLUTION
        # if not nums:
        #     return 0
        # set_nums = set(nums)
        # res = 1
        # for i in set_nums:
        #     if i-1 not in set_nums:
        #         temp_res = 1
        #         temp_val = i + 1
        #         while temp_val in set_nums:
        #             temp_res += 1
        #             temp_val += 1
        #         if res < temp_res:
        #             res = temp_res
        # return res

        # NEETCODE:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # check if it is a start of a sequence
            if n-1 not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest