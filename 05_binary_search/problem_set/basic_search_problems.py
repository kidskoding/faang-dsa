from collections.abc import Callable


def search(nums: list[int], target: int) -> int:
    # Problem 1: Binary Search
    # Key idea: repeatedly cut the sorted search space in half.
    # Time:
    # Space:

    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            return mid

    return -1


def search_insert(nums: list[int], target: int) -> int:
    # Problem 2: Search Insert Position
    # Key idea: find the first index where target could be inserted.
    # Time:
    # Space:

    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            return mid

    return low


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    # Problem 6: Search a 2D Matrix
    # Key idea: treat the row-sorted, column-sorted grid as one flattened sorted array.
    # Time:
    # Space:

    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    low, high = 0, rows * cols - 1
    while low <= high:
        mid = (low + high) // 2
        val = matrix[mid // cols][mid % cols]
        if val > target:
            high = mid - 1
        elif val < target:
            low = mid + 1
        else:
            return True

    return False


def search_matrix_ii(matrix: list[list[int]], target: int) -> bool:
    # Problem 18: Search a 2D Matrix II
    # Key idea: start at a sorted corner and eliminate a full row or column each step.
    # Time:
    # Space:

    if not matrix or not matrix[0]:
        return False

    row, col = 0, len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        val = matrix[row][col]
        if val > target:
            col -= 1
        elif val < target:
            row += 1
        else:
            return True

    return False


def guess_number(n: int, guess: Callable[[int], int]) -> int:
    # Problem 19: Guess Number Higher or Lower
    # Key idea: exact-match search driven by a comparison oracle instead of array reads.
    # Time:
    # Space:

    raise NotImplementedError
