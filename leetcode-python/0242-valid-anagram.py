class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = dict()
        d2 = dict()
        l1 = len(s)
        l2 = len(t)
        if l1 != l2:
            return False
        for i in range(l1):
            if s[i] not in d1.keys():
                d1[s[i]] = 1
            else:
                d1[s[i]] += 1
        for j in range(l2):
            if t[j] not in d2.keys():
                d2[t[j]] = 1
            else:
                d2[t[j]] += 1
        if d1 == d2:
            return True
        return False

    # def isAnagram(self, s: str, t: str) -> bool:
    #     d = dict()
    #     for character in  s:
    #         if character not in d.keys():
    #             d[character] = 1
    #         else:
    #             d[character] += 1
    #     for character in t:
    #         if character not in d.keys():
    #             return False
    #         elif d[character] != 0:
    #             d[character] -= 1
    #             if d[character] == 0:
    #                 del d[character]
    #     if len(d):
    #         return False
    #     return True




