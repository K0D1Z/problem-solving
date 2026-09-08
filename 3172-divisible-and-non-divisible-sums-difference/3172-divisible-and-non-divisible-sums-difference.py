class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = (n * (n + 1)) // 2
        for i in range(0, n + 1, m):
            num1 -= 2*i
        return num1
        