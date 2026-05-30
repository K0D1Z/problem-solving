class Solution:
    def hammingWeight(self, n: int) -> int:
        set_bits = 0
        while n > 0:
            set_bits += n % 2
            n //= 2
        return set_bits
