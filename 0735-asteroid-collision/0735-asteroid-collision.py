class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        
        # MY ATTEMPT
        # stack = []
        # for a in asteroids:
        #     if not stack:
        #         stack.append(a)
        #     elif a < 0:
        #         while stack and stack[-1] > 0 and stack[-1] < abs(a):
        #             stack.pop()
        #         if stack and stack[-1] == abs(a):
        #             stack.pop()
        #         elif (stack and stack[-1] < abs(a)) or not stack:
        #             stack.append(a)
        #     else:
        #         stack.append(a)
        # return stack
                
        # NEETCODE
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()
                
            if a:
                stack.append(a)
                
        return stack
