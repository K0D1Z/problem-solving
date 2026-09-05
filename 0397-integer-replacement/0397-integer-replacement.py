class Solution:
    def integerReplacement(self, n: int) -> int:
        res = 0
        while n != 1:
            if n % 2 == 0:
                n >>= 1
            elif n == 3:
                n -= 1
            elif n & 3 == 3:
                n += 1
            else:
                n -= 1
            res += 1
        return res
        