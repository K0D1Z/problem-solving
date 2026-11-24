class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 4: 1-> 6, 6, 6, ...
        # 4: 2-> 4, 2, 4, 2, 4, 2...
        # 4: 3-> 2, 4, 2, 4, ....
        # 4: 4 -> 6,6,6,6.....

        # 5: 1->8,8
        # 5: 2-> 6, 2, 6, 2
        # 5: 3-> 4, 4, 4
        # 5: 4-> 2, 6, 2, 6
        # 5: 5->8,8,8,8
        if numRows == 1 or numRows >= len(s):
            return s

        res = []
        j = 2 * (numRows - 1)
        mul1 = mul2 = j
        dec = 2
        for i in range(numRows):
            idx = i
            mul1 = j - dec * idx
            mul2 = j - mul1
            if mul1 == 0:
                mul1 = j
            if mul2 == 0:
                mul2 = j

            res.append(s[idx])
            is_mul1 = True
            mul = mul1
            while idx + mul < len(s):
                idx += mul
                res += s[idx]
                if is_mul1:
                    mul = mul2
                else:
                    mul = mul1
                is_mul1 = not is_mul1

        return "".join(res)
            