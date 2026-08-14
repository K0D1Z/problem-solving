class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # EASIEST PYTHON-STYLE APPROACH
        # ans = 2 * nums
        # return ans

        # ALTERNATIVE APPROACH 1
        # ans = nums.copy()
        # for i in nums:
            # ans.append(i)
        # return ans

        # ALTERNATIVE APPROACH 2:
        ans = []
        x = 2
        for _ in range(x):
            for i in nums:
                ans.append(i)
        return ans