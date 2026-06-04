class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return str(bin(n)).count('1') == 1 and n > 0
