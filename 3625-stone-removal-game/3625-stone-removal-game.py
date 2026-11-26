class Solution:
    def canAliceWin(self, n: int) -> bool:
        win = False
        i = 10
        while n - i >= 0:
            n -= i
            win = not win
            i -= 1
        return win
        