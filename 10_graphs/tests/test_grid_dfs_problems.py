from problem_set.grid_dfs_problems import (
    closed_island,
    count_sub_islands,
    flood_fill,
    island_perimeter,
    largest_island,
    max_area_of_island,
    num_enclaves,
    num_islands,
    pacific_atlantic,
    solve,
)


def test_flood_fill_normal_case():
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

    assert flood_fill(image, 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]


def test_flood_fill_already_target_color():
    assert flood_fill([[0, 0, 0]], 0, 0, 0) == [[0, 0, 0]]


def test_flood_fill_single_cell():
    assert flood_fill([[1]], 0, 0, 3) == [[3]]


def test_num_islands_empty_grid():
    assert num_islands([]) == 0


def test_num_islands_single_island():
    grid = [
        ["1", "1", "0", "0"],
        ["1", "1", "0", "0"],
        ["0", "0", "1", "0"],
        ["0", "0", "0", "1"],
    ]

    assert num_islands(grid) == 3


def test_num_islands_no_land():
    assert num_islands([["0", "0"], ["0", "0"]]) == 0


def test_max_area_of_island_normal_case():
    grid = [
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 1, 1, 0],
        [0, 1, 0, 0],
    ]

    assert max_area_of_island(grid) == 5


def test_max_area_of_island_no_land():
    assert max_area_of_island([[0, 0], [0, 0]]) == 0


def test_island_perimeter_single_cell():
    assert island_perimeter([[1]]) == 4


def test_island_perimeter_normal_case():
    grid = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0],
    ]

    assert island_perimeter(grid) == 16


def test_solve_surrounds_enclosed_region():
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    expected = [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]

    solve(board)

    assert board == expected


def test_solve_no_enclosed_region():
    board = [["O", "O"], ["O", "O"]]

    solve(board)

    assert board == [["O", "O"], ["O", "O"]]


def test_pacific_atlantic_normal_case():
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]

    result = pacific_atlantic(heights)

    assert sorted(result) == sorted([[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]])


def test_pacific_atlantic_single_cell():
    assert pacific_atlantic([[1]]) == [[0, 0]]


def test_num_enclaves_normal_case():
    grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]

    assert num_enclaves(grid) == 3


def test_num_enclaves_no_land():
    assert num_enclaves([[0, 0], [0, 0]]) == 0


def test_closed_island_normal_case():
    grid = [
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0],
    ]

    assert closed_island(grid) == 2


def test_closed_island_no_water():
    assert closed_island([[1, 1], [1, 1]]) == 0


def test_count_sub_islands_normal_case():
    grid1 = [
        [1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1],
    ]
    grid2 = [
        [1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1],
        [0, 1, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0],
    ]

    assert count_sub_islands(grid1, grid2) == 3


def test_count_sub_islands_no_islands():
    assert count_sub_islands([[0, 0]], [[0, 0]]) == 0


def test_largest_island_normal_case():
    grid = [[1, 0], [0, 1]]

    assert largest_island(grid) == 3


def test_largest_island_all_land():
    assert largest_island([[1, 1], [1, 1]]) == 4


def test_largest_island_all_water():
    assert largest_island([[0, 0], [0, 0]]) == 1
