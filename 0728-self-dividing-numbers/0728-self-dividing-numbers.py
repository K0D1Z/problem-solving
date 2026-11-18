class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        def isDivisible(n: int) -> bool:
            i = n
            while n != 0:
                t = n % 10
                n //= 10
                if t == 0 or i % t != 0:
                    return False
            return True
        
        res = []
        for i in range(left, right + 1):
            if isDivisible(i):
                res.append(i)

        return res
        