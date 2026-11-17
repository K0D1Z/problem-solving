class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d1 = dict()
        for n in s:
            d1[n] = 1 + d1.get(n, 0)
        d2 = dict()
        for n in t:
            d2[n] = 1 + d2.get(n, 0)

        for k in d2.keys():
            if d1.get(k, 0) != d2.get(k, 0):
                return k
        
        # it is guaranteed that t length is s+1 so i don't worry about outer loop return statement