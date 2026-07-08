def prob01(mat: list[list[int]]) -> list[int]:
    if not mat:
        return []

    if len(mat) == 1:
        return mat[0]

    res = []
    rows, cols = len(mat), len(mat[0])
    up = True

    r, c = 0, 0
    while len(res) < rows * cols:
        res.append(mat[r][c])

        if up:
            if r == 0:
                c += 1
                up = False
            elif c == cols - 1:
                r -= 1
                up = False
            else:
                c += 1
                r -= 1
        else:
            if c == 0:
                r += 1
                up = True
            if r == rows - 1:
                c += 1
                up = True
            else:
                r += 1
                c -= 1

    return res
