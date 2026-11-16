class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def calculateSum(c: str) -> str:
            r = 0
            for i in c:
                r += int(i)
            return str(r)

        while len(s) > k:
            s = "".join([calculateSum(s[i:i+k]) for i in range(0, len(s), k)])
        return s
                
        