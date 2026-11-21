class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row1 = set(list("qwertyuiop"))
        row2 = set(list("asdfghjkl"))
        row3 = set(list("zxcvbnm"))
        rows = [row1, row2, row3]
        res = []
        for w in words:
            for r in rows:
                is_ok = True
                for i in w.lower():
                    if i not in r:
                        is_ok = False
                        break
                if is_ok:
                    res.append(w)
        return res

        