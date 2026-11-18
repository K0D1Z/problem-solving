class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        res = 0
        for n in s:
            if n == 'L':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                res += 1
        return res
        