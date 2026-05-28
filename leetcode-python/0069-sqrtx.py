class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        a = x
        eps = 0.0001
        while True:
            b = (a + x / a) / 2
            if a - b < eps:
                return int(b)
            a = b

