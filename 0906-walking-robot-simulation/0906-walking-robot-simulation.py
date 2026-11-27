class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        obstacle_set: set[tuple[int, int]] = set(map(tuple, obstacles))

        directions: list[tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx: int = 0

        x, y = 0, 0
        max_dist_sq: int = 0

        for cmd in commands:
            if cmd == -1:
                dir_idx = (dir_idx + 1) % 4
            elif cmd == -2:
                dir_idx = (dir_idx - 1) % 4
            else:
                dx, dy = directions[dir_idx]
                for _ in range(cmd):
                    next_x, next_y = x + dx, y + dy
                    if (next_x, next_y) in obstacle_set:
                        break
                    x, y = next_x, next_y
                    max_dist_sq = max(max_dist_sq, x * x + y * y)

        return max_dist_sq