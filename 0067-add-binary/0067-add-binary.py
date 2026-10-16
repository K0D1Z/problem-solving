class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        remainder = 0
        result = ""
        for i in range(1, max_len + 1):
            try:
                n1 = int(a[-i])
            except:
                n1 = 0
            try:
                n2 = int(b[-i])
            except:
                n2 = 0
            number = n1 + n2 + remainder
            result =  str(number % 2) + result
            if number > 1:
                remainder = 1
            else:
                remainder = 0
        if remainder != 0:
            result = "1" + result
        return result