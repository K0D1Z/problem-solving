class Solution:
    def isHappy(self, n: int) -> bool:
        def calculate(number: int) -> int:
            result = 0
            while number != 0:
                digit = number % 10
                number //= 10
                result += digit ** 2
            return result

        hashset = set()
        n = calculate(n)
        while True:
            if n == 1:
                return True
            hashset.add(n)
            n = calculate(n)
            if n in hashset:
                return False