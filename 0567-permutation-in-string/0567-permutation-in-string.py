class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_length = len(s1)
        if window_length > len(s2):
            return False

        hashset1 = dict()
        hashset2 = dict()
        
        for i in range(window_length):
            # print(hashset1, hashset2)
            hashset1[s1[i]] = 1 + hashset1.get(s1[i], 0)
            hashset2[s2[i]] = 1 + hashset2.get(s2[i], 0)
        
        for i in range(window_length, len(s2)):
            # print(hashset1, hashset2)
            if hashset1 == hashset2:
                return True
            hashset2[s2[i-window_length]] -= 1
            if hashset2[s2[i-window_length]] == 0:
                del hashset2[s2[i-window_length]]
            hashset2[s2[i]] = 1 + hashset2.get(s2[i], 0)
        
        if hashset1 == hashset2:
            return True
            
        return False

        