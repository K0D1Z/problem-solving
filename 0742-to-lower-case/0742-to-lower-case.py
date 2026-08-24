class Solution:
    def toLowerCase(self, s: str) -> str:
        # bozo solution
        # return s.lower()

        res = ""
        for l in s:
            c = chr(ord(l) + (ord("a") - ord("A"))) if ord('Z') >= ord(l) >= ord("A") else l
            res += c
        return res
        