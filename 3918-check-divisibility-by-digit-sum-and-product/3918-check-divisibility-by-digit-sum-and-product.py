class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum_n = 0
        prod_n = 1
        copy_n = n
        while copy_n != 0:
            remainder = copy_n % 10
            copy_n //= 10
            prod_n *= remainder
            sum_n += remainder
        return (n % (sum_n + prod_n)) == 0