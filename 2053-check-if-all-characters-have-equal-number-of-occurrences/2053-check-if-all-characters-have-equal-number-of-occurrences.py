class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hashmap = dict()
        for i in s:
            hashmap[i] = 1 + hashmap.get(i, 0)
        return len(set(hashmap.values())) == 1
        