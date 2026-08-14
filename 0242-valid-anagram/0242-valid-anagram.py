class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # PYTHON STYLE
        # return Counter(s) == Counter(t)

        # SORTING SOLUTION
        # return sorted(s) == sorted(t)

        # HASHMAP SOLTUTION
        if len(s) != len(t):
            return False

        hashmap_1 = {}
        hashmap_2 = {}

        for i in range(len(s)):
            hashmap_1[s[i]] = 1 + hashmap_1.get(s[i], 0)
            hashmap_2[t[i]] = 1 + hashmap_2.get(t[i], 0)
        
        for c in hashmap_1:
            if hashmap_1.get(c, 0) != hashmap_2.get(c, 0):
                return False

        return True

   