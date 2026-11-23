class Solution:
    def frequencySort(self, s: str) -> str:
        h = dict()
        for i in s:
            h[i] = 1 + h.get(i, 0)
        
        res = ""
        h = sorted(h.items(), key=lambda item: item[1], reverse=True)
        print(h)
        for i, v in h:
            res += i * v
        return res

