class Solution:
    def minElement(self, nums: List[int]) -> int:
        new_list = []
        for i in nums:
            temp_sum = 0
            while i != 0:
                temp_sum += i % 10
                i //= 10
            new_list.append(temp_sum)
        return min(new_list)
