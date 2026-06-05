from collections import deque

# Problem 1: Flood Fill

# Time: O(r * c) - In the worst case we traverse through all the cells in the grid,
# which can be represented by r * c
# 
# Space: O(r * c) - Each queued item is a coordinate pair of (r, c) and there can be
# up to r * c cells discovered during the traversal
def prob01(image, sr, sc, color):
    # 1. Let original_color be the original color that consists of the color in the starting cell (image[sr][sc])
    original_color = image[sr][sc]

    # 2. If the original_color is equal to the target color (color), then no changes are made to the image and we can just
    # return the image itself (by definition of the problem)
    if original_color == color:
        return image

    # 3. Begin by assigning the first pixel value to the targeted color
    image[sr][sc] = color

    # 4. Let dirs represent all the possible directions to traverse in the grid
    # By definition of the problem, we can traverse through all the possible directions in up, down, left, and right
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # 5. Begin a BFS traversal on the image grid, where we use a queue to process each level in the grid
    def bfs():
        # 6. Let rows and cols be the number of rows and columns in the grid respectively
        rows, cols = len(image), len(image[0])

        # 7. Build a queue, which will process each row of the grid level by level
        # Let the queue begin with the starting coordinates of sr and sc
        queue = deque([(sr, sc)])

        # 8. Process each level of the queue
        while queue:
            # 9. Let r and c be the row and column of the most current coordinate added to the queue
            r, c = queue.popleft()
            
            for dr, dc in dirs:
                # 10. Let nr and nc be the new row and new column after applying the new direction 
                nr, nc = r + dr, c + dc

                # 11. Check if nr and nc are within appropriate bounds
                # We know that if nr and nc are within appropriate bounds of 0 and rows
                # and 0 and cols respectively and the current cell matches the original color,
                # then we can modify it to be the target color
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original_color:
                    # 12. Color the updated cell to the target color
                    image[nr][nc] = color

                    # 13. 
                    queue.append((nr, nc))

        # 14. Return the updated image grid
        return image

    return bfs()

# Alternative DFS Solution for Flood Fill
def dfs():
    pass
