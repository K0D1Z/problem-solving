class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def isPilesEaten(k):
            res = 0
            for i in piles:
                res += math.ceil(i / k)
                if res > h:
                    return False
            return True

        l = 1
        r = max(piles)
        k = float('inf')
        while l <= r:
            m = (l + r) // 2
            if isPilesEaten(m):
                k = min(k, m)
                r = m - 1
            else:
                l = m + 1

        return k

