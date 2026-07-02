from collections import deque

# Problem 2: Rotting Oranges


def prob02(grid: list[list[int]]) -> int:
    if not grid:
        return -1

    queue = deque()
    minutes, fresh = 0, 0
    rows, cols = len(grid), len(grid[0])
    dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            else:
                fresh += 1

    if fresh == 0:
        return 0

    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    grid[nr][nc] = 2
                    queue.append((nr, nc))
                    fresh -= 1

            minutes += 1

    return minutes - 1 if fresh == 0 else -1
