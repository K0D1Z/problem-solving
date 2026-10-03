class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        hashmap_t = dict()
        hashmap_window = dict()

        for x in t:
            hashmap_t[x] = 1 + hashmap_t.get(x, 0)
        
        have, need = 0, len(hashmap_t)
        res, res_len = [-1, -1], float('inf')
        l = 0

        for r in range(len(s)):
            c = s[r]
            hashmap_window[c] = 1 + hashmap_window.get(c, 0)
            if c in hashmap_t and hashmap_window[c] == hashmap_t[c]:
                have += 1
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                p = s[l]
                hashmap_window[p] -= 1
                if p in hashmap_t and hashmap_window[p] < hashmap_t[p]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""
