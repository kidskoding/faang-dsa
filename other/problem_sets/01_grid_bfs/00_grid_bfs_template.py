from collections import deque


def grid_bfs(grid, start_r, start_c):
    """
    General BFS template for grid problems.

    Use this when you need to start from one cell and explore neighboring cells
    level by level. Examples: flood fill, shortest path in a grid, rotting
    oranges, walls and gates, and island traversal.
    """
    rows, cols = len(grid), len(grid[0])

    # Four-directional movement: right, left, down, up.
    # Use eight directions only if the problem allows diagonals.
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # BFS starts by putting the starting cell in the queue.
    queue = deque([(start_r, start_c)])

    # Mark the starting cell as visited immediately.
    # This is important because a neighbor could otherwise add it again later.
    visited = set()
    visited.add((start_r, start_c))

    while queue:
        # Pop the next cell whose neighbors we are ready to explore.
        r, c = queue.popleft()

        # This is where you process the current cell if the problem needs it.
        # Examples:
        # - count this cell as part of an island
        # - update an answer using grid[r][c]
        # - check whether this cell is the target in a shortest path problem

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            # First check bounds. Never read grid[nr][nc] before this.
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue

            # Then check whether this neighbor is allowed by the problem.
            # Replace this with the real condition.
            #
            # Examples:
            # - flood fill: grid[nr][nc] == original_color
            # - islands: grid[nr][nc] == "1"
            # - binary matrix path: grid[nr][nc] == 0
            if not is_valid_neighbor(grid, nr, nc):
                continue

            # Then check whether we have already discovered this cell.
            # A cell is "discovered" once we decide it should be visited.
            if (nr, nc) in visited:
                continue

            # Standard BFS rule:
            # discover valid neighbor -> mark visited -> add to queue
            #
            # Marking visited before enqueueing prevents the same cell from
            # being added multiple times by different neighboring cells.
            visited.add((nr, nc))
            queue.append((nr, nc))

    return visited


def is_valid_neighbor(grid, r, c):
    """
    Placeholder condition for the template.

    Replace this function with the rule from the specific problem.
    """
    return True


def flood_fill_style_bfs(image, sr, sc, color):
    """
    Flood fill version of the same BFS template.

    In flood fill, we do not need a separate visited set because recoloring a
    cell also marks it as visited.
    """
    original_color = image[sr][sc]

    if original_color == color:
        return image

    rows, cols = len(image), len(image[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    queue = deque([(sr, sc)])

    # Mark the start cell as visited by recoloring it immediately.
    image[sr][sc] = color

    while queue:
        r, c = queue.popleft()

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < rows and 0 <= nc < cols):
                continue

            # In flood fill, a neighbor is valid only if it still has the
            # original color. If it already has the new color, it has either
            # been visited or was never part of the fill region.
            if image[nr][nc] != original_color:
                continue

            # This line is the visited marker for flood fill.
            # We recolor before enqueueing so another neighbor cannot enqueue
            # the same cell again.
            image[nr][nc] = color

            # Add the discovered cell so BFS can later explore its neighbors.
            queue.append((nr, nc))

    return image
