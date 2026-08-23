class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashmap = dict()
        s = s.split(" ")
        if len(set(s)) != len(set(list(pattern))) or len(s) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in hashmap:
                hashmap[pattern[i]] = s[i]
            if hashmap[pattern[i]] != s[i]:
                return False
        
        return True