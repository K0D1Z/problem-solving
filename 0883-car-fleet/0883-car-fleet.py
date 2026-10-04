class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # stack = sorted([(position[i], speed[i]) for i in range(len(position))], key=lambda x: x[0])
        pair = [[p, s] for p, s in zip(position, speed)]
        pair = sorted(pair)[::-1]
        stack = []

        for p, s in pair:
            time = (target - p) / s
            stack.append(time)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
