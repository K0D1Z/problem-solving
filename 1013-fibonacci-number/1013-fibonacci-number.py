class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        n1 = 0
        n2 = 1
        for _ in range(n):
            n1, n2 = n2, n1+n2

        return n1

        