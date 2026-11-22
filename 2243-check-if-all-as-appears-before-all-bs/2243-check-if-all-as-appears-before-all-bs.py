class Solution:
    def checkString(self, s: str) -> bool:
        b_found = False
        a_found = False
        for i in s:
            if i == 'b':
                b_found = True
            if b_found and i == 'a':
                return False
        return True
        