from collections import defaultdict
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        def getLargestDigit(n: int) -> int:
            res = 0
            while n > 0:
                res = max(res, n % 10)
                n //= 10
            return res

        d = defaultdict(list)
        res = -1
        for n in nums:
            l = getLargestDigit(n)
            if len(d[l]) in (0, 1):
                d[l].append(n)
            else:
                if d[l][0] > d[l][1]:
                    d[l][1] = max(d[l][1], n)
                else:
                    d[l][0] = max(d[l][0], n)
        
        for v in d.values():
            if len(v) == 2:
                res = max(sum(v), res)
        return res
