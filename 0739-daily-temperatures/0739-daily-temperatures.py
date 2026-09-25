class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = [] # pair of values (temperature, index)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_temp, stack_idx = stack.pop()
                res[stack_idx] = i - stack_idx
            stack.append((t, i))
        return res


