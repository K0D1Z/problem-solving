class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        n = []
        for i in range(len(s)):
            if s[i] == goal[0]:
                n.append(i)

        if not n:
            return False

        l = len(s)

        for j in n:
            found = True
            for i in range(l):
                if s[(i + j) % l] != goal[i]:
                    found = False
            if found:
                return True
                    
        return False

        