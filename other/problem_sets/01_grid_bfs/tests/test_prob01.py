from prob01 import prob01


def test_flood_fill_recolors_connected_component():
    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1],
    ]

    result = prob01(image, 1, 1, 2)

    assert result == [
        [2, 2, 2],
        [2, 2, 0],
        [2, 0, 1],
    ]
    assert result is image


def test_flood_fill_same_color_returns_image_unchanged():
    image = [
        [0, 0, 0],
        [0, 1, 1],
    ]

    result = prob01(image, 1, 1, 1)

    assert result == [
        [0, 0, 0],
        [0, 1, 1],
    ]
    assert result is image


def test_flood_fill_does_not_cross_different_colors():
    image = [
        [1, 1, 0, 1],
        [1, 0, 0, 1],
        [0, 0, 1, 1],
    ]

    result = prob01(image, 0, 0, 9)

    assert result == [
        [9, 9, 0, 1],
        [9, 0, 0, 1],
        [0, 0, 1, 1],
    ]


def test_flood_fill_single_cell():
    image = [[3]]

    result = prob01(image, 0, 0, 7)

    assert result == [[7]]
