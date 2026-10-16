class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        list_of_prime_factors = [2, 3, 5]
        for num in list_of_prime_factors:
            while n % num == 0:
                n //= num
        return True if n == 1 else False