class Solution:
    def minChanges(self, s: str) -> int:
        t = []
        for i in range(1, len(s), 2):
            # print(s[i-1] + s[i])
            if s[i] == s[i - 1]:
                t.append(0)
            else:
                t.append(1)
        return sum(t)
        