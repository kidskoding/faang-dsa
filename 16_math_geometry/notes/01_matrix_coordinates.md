# Matrix Coordinates and In-Place Transforms

A **matrix** is a `list[list[...]]` addressed by two numbers instead of one, so
`matrix[r][c]` names the cell in row `r` and column `c`. The row index always
comes first, `len(matrix)` counts rows, and `len(matrix[0])` counts columns

```text
          c=0  c=1  c=2
   r=0 [   1    2    3  ]
   r=1 [   4    5    6  ]
   r=2 [   7    8    9  ]

matrix[1][2] is 6
```

An **index transform** is a rule that says where the value sitting at one
position belongs afterwards. You have already used a one-dimensional one, since
reversing an array sends the value at index `i` to index `n - 1 - i`. A matrix
transform is the same kind of rule with two coordinates. Rotating a square
matrix a quarter turn clockwise sends the value at `(r, c)` to `(c, n - 1 - r)`,
because the top row has to stand up as the rightmost column

The important property of every transform in this topic is that it is a
**permutation** of the positions. No cell is created and no cell is destroyed,
because the values are only relabelled with new addresses. That sounds
harmless, and it is exactly what makes rearranging a matrix in place harder
than it looks

You walked grids in [grid DFS](../../10_graphs/notes/02_grid_dfs.md) and
[grid BFS](../../10_graphs/notes/03_grid_bfs.md), where a cell was read, tested,
and at most marked as seen. This topic is about the problems where the cells
themselves have to move, or where the grid has to hold a second piece of
information alongside its own values, without allocating a second grid

## The Cell You Overwrite Is Somebody Else's Input

The naive way to apply a transform in place is to write the formula down and
run it. For a clockwise rotation, walk every position and copy its value to
`(c, n - 1 - r)`

```python
def rotate_naive(matrix: list[list[int]]) -> None:
    n = len(matrix)
    for r in range(n):
        for c in range(n):
            matrix[c][n - 1 - r] = matrix[r][c]


broken = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate_naive(broken)
assert broken == [[7, 4, 1], [2, 5, 2], [1, 2, 1]]
assert broken != [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

nothing: list[list[int]] = []
rotate_naive(nothing)
assert nothing == []
```

The asserts record what it actually does rather than what it should. The first
row comes out right and everything after it is garbage, with 2 appearing three
times and 3, 6, 8 and 9 gone entirely

The reason is visible on the very first write. Position `(0, 0)` holds 1 and its
destination is `(0, 2)`, which currently holds 3. The write lands, 3 is gone, and
the loop reaches `(0, 2)` two steps later and copies the 1 that is now sitting
there into 3's destination

```text
before        after writing (0,0) -> (0,2)
1  2  3       1  2  1        3 is destroyed, and it never got to move
4  5  6       4  5  6
7  8  9       7  8  9
```

The transform is correct. The problem is the **order** of the writes, and there
is no scan order that fixes it, because the destinations form cycles: `(0, 0)`
sends to `(0, 2)`, which sends to `(2, 2)`, which sends to `(2, 0)`, which sends
back to `(0, 0)`. Whichever cell in a cycle you write first destroys the value
the next one needs

That single failure is what the rest of this topic answers, and the answers come
in three shapes:

- **Swap rather than write.** A swap moves two values at once and loses nothing,
  so a transform built only out of swaps is safe in any order
- **Put the extra information where nothing has read it yet.** If you need to
  remember something about the grid, keep it in a region you have already
  consumed or have not yet consumed
- **Store both states in one cell.** An `int` cell has bits to spare, so the old
  value and the new value can live in the same slot until every reader is done

## Rotating By Reflecting Twice

The fix for rotation is to decompose the transform into two passes that are each
made of swaps. The first is the **transpose**, which reflects the matrix across
its main diagonal by exchanging `matrix[r][c]` with `matrix[c][r]`

```text
original           transposed         then reverse each row
1  2  3            1  4  7            7  4  1
4  5  6     ->     2  5  8      ->    8  5  2
7  8  9            3  6  9            9  6  3
```

The transpose puts the right values in the right *rows* but in mirrored order,
because column `c` of the original became row `c` read top to bottom, while a
clockwise rotation needs it read bottom to top. Reversing each row flips exactly
that, and a row reversal is itself a sequence of swaps, so both passes are safe

> "A rotation is a permutation with cycles in it, so writing cells one at a time
> clobbers values I still need. I will do it as a transpose followed by a row
> reversal instead, because both of those are built from swaps and a swap never
> loses a value."

```python
def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)

    for r in range(n):
        for c in range(r + 1, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    for row in matrix:
        row.reverse()


grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(grid)
assert grid == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

two = [[1, 2], [3, 4]]
rotate(two)
assert two == [[3, 1], [4, 2]]

single = [[5]]
rotate(single)
assert single == [[5]]

empty: list[list[int]] = []
rotate(empty)
assert empty == []
```

**The inner range is the line people get wrong.** It is `range(r + 1, n)`, so the
swap only ever fires for positions strictly above the diagonal. Writing
`range(n)` instead visits every pair twice, once as `(r, c)` and once as
`(c, r)`, and the second swap undoes the first. That version returns
`[[1, 2, 3], [4, 5, 6], [7, 8, 9]]` on the example above, which is the input
unchanged and looks like the function was never called. Starting at `r + 1` also
skips `(r, r)`, which is correct because a diagonal cell is its own reflection

The counterclockwise version is the same two passes with the second one changed.
Transpose, then reverse the **order of the rows** rather than the contents of
each row, which is one call:

```python
def rotate_ccw(matrix: list[list[int]]) -> None:
    n = len(matrix)

    for r in range(n):
        for c in range(r + 1, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    matrix.reverse()


grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate_ccw(grid)
assert grid == [[3, 6, 9], [2, 5, 8], [1, 4, 7]]

single = [[7]]
rotate_ccw(single)
assert single == [[7]]
```

`matrix.reverse()` reverses the outer list, so it reorders whole rows and moves
no individual cell, whereas `row.reverse()` inside the loop reorders the cells of
one row. Mixing those two up is the single most common rotation bug, and the
symptom is an answer rotated the wrong way rather than an exception

## Shrinking Four Boundaries Instead Of Tracking Visited Cells

Reading a matrix in spiral order means walking the outer ring clockwise, then the
next ring in, and so on until nothing is left. The obvious approach is to walk
with a direction and turn right whenever the next cell is off the grid or already
visited, which needs a full `R * C` visited grid to know where you have been

You do not need it, because the visited cells are never scattered. After the top
row is consumed, everything unvisited sits strictly below it, so the entire
"where have I been" state is four integers naming the still-unread rectangle

```text
top    -> +-----------------+
          | 1   2   3   4   |
          | 5   6   7   8   |
          | 9  10  11  12   |
bottom -> +-----------------+
          ^                 ^
        left              right

after the top row is read, top becomes 1 and the rectangle is rows 1..2
```

Each of the four passes walks one side of that rectangle and then retires the
line it just consumed by moving its boundary inward by one

```python
def spiral_order(matrix: list[list[int]]) -> list[int]:
    if not matrix or not matrix[0]:
        return []

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    out: list[int] = []

    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            out.append(matrix[top][c])
        top += 1

        for r in range(top, bottom + 1):
            out.append(matrix[r][right])
        right -= 1

        if top <= bottom:
            for c in range(right, left - 1, -1):
                out.append(matrix[bottom][c])
            bottom -= 1

        if left <= right:
            for r in range(bottom, top - 1, -1):
                out.append(matrix[r][left])
            left += 1

    return out


assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert spiral_order([[1, 2, 3]]) == [1, 2, 3]
assert spiral_order([[1], [2], [3]]) == [1, 2, 3]
assert spiral_order([]) == []
assert spiral_order([[]]) == []
```

**Why the third and fourth passes are guarded and the first two are not.** The
`while` condition was checked before the top row ran, so passes one and two are
known to have a line to walk. Passes three and four run after two boundaries have
already moved, so the rectangle may have collapsed mid-iteration, and walking a
line that no longer exists re-reads cells the first two passes already took.
Without `if top <= bottom`, the single-row input `[[1, 2, 3]]` returns
`[1, 2, 3, 2, 1]`, because the bottom pass walks the same and only row backwards

> "The four boundaries are the state, so I do not need a visited grid. I do need
> the two guards before the bottom and left passes, because after `top` and
> `right` move the rectangle can already be empty, and a single-row input would
> otherwise be read twice."

### Dry Run: Spiral Order On A 3x3

```text
start                     top=0 bottom=2 left=0 right=2   out=[]

top row, c 0..2           out=[1,2,3]        top=1
right col, r 1..2         out=[..,6,9]       right=1
top<=bottom (1<=2) yes
bottom row, c 1..0        out=[..,8,7]       bottom=1
left<=right (0<=1) yes
left col, r 1..1          out=[..,4]         left=1

while (1<=1 and 1<=1) yes
top row, c 1..1           out=[..,5]         top=2
right col, r 2..1 empty   out unchanged      right=0
top<=bottom (2<=1) NO     REJECTED, bottom pass skipped
left<=right (1<=0) NO     REJECTED, left pass skipped

while (2<=1) false        stop
out=[1,2,3,6,9,8,7,4,5]
```

The two rejections are the whole reason the guards exist. When the centre cell 5
was read, `top` moved past `bottom`, so the rectangle was empty from that moment
on. The bottom pass would have walked row `bottom = 1` again and appended 5 a
second time. Notice also the right-column pass on that same iteration ran with an
empty `range(2, 2)` and needed no guard, because an empty `range` is already a
no-op, whereas the two reversed loops count *downwards* and stay non-empty even
when the rectangle has collapsed

The same four boundaries generate a spiral instead of reading one. Nothing about
the walk changes, because only the body of each loop flips from `append` to an
assignment

```python
def generate_matrix(n: int) -> list[list[int]]:
    grid = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    value = 1

    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            grid[top][c] = value
            value += 1
        top += 1

        for r in range(top, bottom + 1):
            grid[r][right] = value
            value += 1
        right -= 1

        if top <= bottom:
            for c in range(right, left - 1, -1):
                grid[bottom][c] = value
                value += 1
            bottom -= 1

        if left <= right:
            for r in range(bottom, top - 1, -1):
                grid[r][left] = value
                value += 1
            left += 1

    return grid


assert generate_matrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
assert generate_matrix(1) == [[1]]
assert generate_matrix(0) == []
```

Recognising that two problems are one skeleton with a different loop body is
worth saying out loud, because it turns a second problem into a thirty-second
answer

## Storing The Marks Inside The Grid

[Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) asks you to
zero out the entire row and entire column of every cell that holds a zero. The
trap is that zeroing as you go is destructive in the sense the first section
warned about: a freshly written zero is indistinguishable from an original zero,
so the second row you process zeroes rows that were never supposed to move

Collecting the rows and columns to zero into two sets fixes that and costs
`O(R + C)` space, which is the answer most people give. The follow-up asks for
`O(1)`, and the way to get it is to keep those two sets inside the grid. Row 0
becomes the list of columns to zero, and column 0 becomes the list of rows to
zero, since both of those regions are going to be zeroed anyway if they contain
a zero themselves

There is one conflict, and it is the whole difficulty. Cell `(0, 0)` sits in both
marker regions, so it would have to mean "row 0 contains a zero" and "column 0
contains a zero" at the same time, and one cell cannot hold two independent
facts. On `[[1, 0], [1, 1]]` the correct answer is `[[0, 0], [1, 0]]`, but a
version that lets `(0, 0)` carry both meanings returns `[[0, 0], [0, 0]]`,
because the marker written for row 0 gets read back as a marker for column 0

Pull one of the two facts out into a plain boolean before the scan starts

```python
def set_zeroes(matrix: list[list[int]]) -> None:
    if not matrix or not matrix[0]:
        return

    rows, cols = len(matrix), len(matrix[0])
    first_col_has_zero = any(matrix[r][0] == 0 for r in range(rows))

    for r in range(rows):
        for c in range(1, cols):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0

    for r in range(rows - 1, -1, -1):
        for c in range(cols - 1, 0, -1):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0
        if first_col_has_zero:
            matrix[r][0] = 0


g = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12]]
set_zeroes(g)
assert g == [[0, 0, 3, 4], [0, 0, 0, 0], [0, 0, 0, 0]]

small = [[1, 0], [1, 1]]
set_zeroes(small)
assert small == [[0, 0], [1, 0]]

untouched = [[1]]
set_zeroes(untouched)
assert untouched == [[1]]

nothing: list[list[int]] = []
set_zeroes(nothing)
assert nothing == []
```

**Three decisions carry this**:

- The scan starts at `c = 1`, because column 0 is a marker region and its own
  zeros are already recorded in `first_col_has_zero`. Scanning from `c = 0` would
  write a row marker into a cell that is also being read as a column marker
- The write phase runs **bottom to top**, because row 0 is still holding the
  column markers that every other row depends on. Zeroing row 0 first would erase
  them, and the rows below would then see a clean marker row and change nothing
- Column 0 of each row is written **after** that row's other cells and only from
  the boolean, because `matrix[r][0]` is that row's marker and must stay readable
  until the row is finished

### Dry Run: Marking Without A Second Grid

```text
input
1   2   3   4
5   0   7   8
0  10  11  12

first_col_has_zero = True         because matrix[2][0] is 0

scan c >= 1
(0,1)..(0,3)  nonzero             nothing marked
(1,1) is 0    matrix[1][0] = 0    row 1 is marked
              matrix[0][1] = 0    column 1 is marked
(1,2),(1,3)   nonzero             nothing marked
(2,0)         NOT SCANNED         column 0 is a marker region, the boolean has it
(2,1)..(2,3)  nonzero             nothing marked

markers now
1   0   3   4
0   0   7   8
0  10  11  12

write phase, rows 2 then 1 then 0, columns 3 down to 1, then column 0
row 2   matrix[2][0] is 0 -> zero the row, then column 0 from the boolean
row 1   matrix[1][0] is 0 -> zero the row, then column 0 from the boolean
row 0   matrix[0][1] is 0 -> only that column zeroes, then column 0

result
0   0   3   4
0   0   0   0
0   0   0   0
```

The skipped cell `(2, 0)` is the one to look at. It is an original zero, and
nothing in the scan phase touched it, because the scan deliberately never reads
column 0. Its effect reached the answer entirely through `first_col_has_zero`,
which was computed before any write happened. Had the scan included column 0, it
would have written `matrix[0][0] = 0`, and the write phase would then have read
that as "column 0 is marked" and also as "row 0 is marked", zeroing row 0
entirely and losing the 3 and the 4

## Worked Example: [Game of Life](https://leetcode.com/problems/game-of-life/)

Every cell of a board is either live or dead, and the whole board advances one
generation at once. A live cell stays alive only when exactly two or three of its
eight neighbours are live, and a dead cell becomes live only when exactly three
of its neighbours are live. Every cell's next value is decided from the current
board, so no update may be visible to another cell's calculation

**Input**: `board`, a `list[list[int]]` where `board[r][c]` is `1` for a live
cell and `0` for a dead one, with `len(board)` rows and `len(board[0])` columns.
Cells outside the board do not exist and count as nothing rather than as dead
neighbours, which is the same thing numerically but a different sentence to say
out loud

**Output**: none. The function returns `None`, and the answer is the mutation of
`board` itself, which afterwards holds `1` and `0` describing the **next**
generation rather than the current one. The follow-up asks for this to happen
without allocating a second board

Copying the board and reading the copy while writing the original is correct and
costs `O(R * C)` extra space. Writing straight into `board` without a copy is the
failure from the first section again: the moment cell `(0, 0)` takes its new
value, cell `(0, 1)` counts it as a neighbour and reads next-generation data as
if it were current

The values only ever need one bit, so the cell has room for two. Keep the current
state in bit 0, where it already is, and write the next state into bit 1. Reading
`board[r][c] & 1` then returns the current state no matter whether that cell has
been decided yet, and a final pass of `board[r][c] >>= 1` promotes every next
state down into bit 0. The bitwise operators are the ones from
[bitwise basics](../../15_bit_manipulation/notes/01_bitwise_basics.md)

```text
cell value   bit 1   bit 0     meaning
    0          0       0       dead now, dead next
    1          0       1       live now, dies next
    2          1       0       dead now, born next
    3          1       1       live now, survives next
                ^
        the bit written this pass, invisible to every & 1 read
```

> "I cannot write the answer into a cell that neighbours still have to read, so I
> will encode both generations at once. Bit 0 stays the current state, bit 1
> holds the next state, every neighbour count masks with `& 1`, and one final
> right shift makes the next generation the only one left."

Therefore,

1. Guard the empty and empty-row cases first, because the next step reads
   `len(board[0])` and an empty board has no row 0 to measure
2. Walk every cell in any order, since the encoding makes order irrelevant, and
   count its live neighbours by trying all eight `(dr, dc)` offsets, skipping
   `(0, 0)` because a cell is not its own neighbour and bounds-checking each one
   before indexing
3. Add `board[nr][nc] & 1` rather than `board[nr][nc]` to the count. That mask is
   the load-bearing line, because a neighbour already decided this pass may hold
   `2` or `3`, and `& 1` recovers the current state it had before this pass began
4. Apply the two rules. A cell that is currently live, meaning `board[r][c] & 1`
   is set, survives on a count of exactly two or three, and a currently dead cell
   is born on a count of exactly three
5. Record a survival or a birth with `board[r][c] |= 2`, which sets bit 1 and
   leaves bit 0 alone. Cells that die or stay dead need no write at all, because
   bit 1 is already `0`, and this is why the code has no `else` branch
6. Finish with a second full pass of `board[r][c] >>= 1`, which discards the old
   state in bit 0 and slides the next state down into it, leaving every cell as a
   plain `0` or `1` again

```python
def game_of_life(board: list[list[int]]) -> None:
    if not board or not board[0]:
        return

    rows, cols = len(board), len(board[0])

    for r in range(rows):
        for c in range(cols):
            live = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        live += board[nr][nc] & 1

            if board[r][c] & 1:
                if live == 2 or live == 3:
                    board[r][c] |= 2
            elif live == 3:
                board[r][c] |= 2

    for r in range(rows):
        for c in range(cols):
            board[r][c] >>= 1


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
game_of_life(board)
assert board == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

block = [[1, 1], [1, 0]]
game_of_life(block)
assert block == [[1, 1], [1, 1]]

lonely = [[1]]
game_of_life(lonely)
assert lonely == [[0]]

nothing: list[list[int]] = []
game_of_life(nothing)
assert nothing == []
```

### Dry Run: One Generation Of The Glider

```text
input board            live neighbour counts
0  1  0                1  1  2
0  0  1                3  5  3
1  1  1                1  3  2
0  0  0                2  3  2

after the encoding pass
0  1  0        (0,1) is live with 1 neighbour  -> REJECTED, no bit 1 written
2  0  3        (1,0) is dead with 3            -> born,     value 0 | 2 = 2
1  3  3        (1,2) is live with 3            -> survives, value 1 | 2 = 3
0  2  0        (2,0) is live with 1            -> REJECTED, stays 1

after >>= 1
0  0  0
1  0  1
0  1  1
0  1  0
```

The rejected cells are the ones that prove the encoding works. Cell `(0, 1)` is
live but has only one live neighbour, so it fails the survival rule and no bit is
written, leaving it at `1`. Two steps later, cell `(1, 1)` counts its neighbours
and reads `board[0][1] & 1`, which is still `1`, so `(0, 1)` correctly
contributes to that count even though it has already been judged and condemned.
Cell `(1, 0)` shows the other direction: it was written as `2` early in the pass,
and every later neighbour reading it gets `2 & 1 == 0`, which is its dead current
state rather than its live next state

- **Time Complexity:** `O(R * C)`, where `R` is the number of rows and `C` the
  number of columns, because each of the `R * C` cells does a fixed eight-offset
  neighbour count in the first pass and one shift in the second
- **Space Complexity:** `O(1)` auxiliary, because the next generation is stored
  in bit 1 of the cells that already exist and the only extra variables are the
  loop counters and one neighbour tally

## Time and Space Complexity

`n` is the side length of a square matrix. `R` and `C` are the number of rows and
columns of a rectangular one, so `R * C` is the number of cells

**Rotating a square matrix a quarter turn**

| Approach                                                            | Time                                                                                                                 | Space                                                                                      |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Copy into a fresh matrix with `result[c][n - 1 - r] = matrix[r][c]` | `O(n²)`: one write per cell, and the destination formula makes each write `O(1)`                                     | `O(n²)`: a second matrix of the same size, which is what the in-place follow-up forbids    |
| Transpose then reverse each row                                     | `O(n²)`: the transpose swaps the `n(n - 1) / 2` positions above the diagonal and the reversals touch every cell once | `O(1)` auxiliary: only loop indices, since every move is a swap inside the original matrix |

**Reading a matrix in spiral order**

| Approach                                         | Time                                                                                            | Space                                                                                                |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Walk with a direction and turn at a visited cell | `O(R * C)`: every cell is visited once and each turn test is `O(1)`                             | `O(R * C)`: a full parallel grid of booleans to remember where the walk has been                     |
| Four shrinking boundaries                        | `O(R * C)`: each cell is appended exactly once and each boundary moves at most `R` or `C` times | `O(1)` auxiliary beyond the output list, because the four integers replace the visited grid entirely |

**Zeroing the row and column of every zero**

| Approach                                   | Time                                                                                  | Space                                                                                             |
| ------------------------------------------ | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Collect the rows and columns into two sets | `O(R * C)`: one scan to fill the sets and one to write, each visiting every cell once | `O(R + C)`: worst case every row and every column is marked, so both sets fill up                 |
| Mark inside row 0 and column 0             | `O(R * C)`: the same two passes, with the marker reads costing `O(1)` each            | `O(1)` auxiliary: one boolean for column 0, since the markers live in cells the grid already owns |

**Advancing one Game of Life generation**

| Approach                             | Time                                                                                                              | Space                                                                                       |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Read a deep copy, write the original | `O(R * C)`: eight neighbour reads per cell is a constant factor                                                   | `O(R * C)`: the copy duplicates every cell, which the follow-up rules out                   |
| Two bits per cell                    | `O(R * C)`: the same eight reads per cell, plus one extra full pass of shifts, which is still linear in the cells | `O(1)` auxiliary: bit 1 of each existing cell holds the next state, so nothing is allocated |

## Summary

- A **matrix** is indexed `matrix[row][column]` with the row first, `len(matrix)`
  rows and `len(matrix[0])` columns. An **index transform** is the rule saying
  where the value at `(r, c)` belongs afterwards, such as `(c, n - 1 - r)` for a
  quarter turn clockwise
  - Every transform in this family is a permutation of positions, so nothing is
    created or destroyed, only readdressed
- Applying a transform by writing each cell straight to its destination corrupts
  the matrix, because the destinations form cycles and the first write in a cycle
  destroys the value the next write needs. This is the single failure the whole
  topic is organised around
  - The naive clockwise rotation of `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]` returns
    `[[7, 4, 1], [2, 5, 2], [1, 2, 1]]`, with three copies of 2 and no 3, 6, 8
    or 9
- Rotate a square matrix in place by transposing it and then reversing each row,
  because a transpose and a reversal are both made only of swaps, and a swap
  moves two values simultaneously so it can never lose one
  - The transpose loop must be `for c in range(r + 1, n)`. Using `range(n)` swaps
    every pair twice and leaves the matrix exactly as it started
  - Counterclockwise is transpose plus `matrix.reverse()`, which reorders whole
    rows, as opposed to `row.reverse()`, which reorders the cells inside one row
- Spiral traversal needs no visited grid, because the unread cells always form a
  rectangle, so `top`, `bottom`, `left` and `right` are the complete state. Walk
  one side, then move that boundary inward by one
  - Guard the bottom and left passes with `if top <= bottom` and
    `if left <= right`, since two boundaries have already moved by then and the
    rectangle may be empty. Without the first guard, `[[1, 2, 3]]` returns
    `[1, 2, 3, 2, 1]`
  - [Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/) is the
    identical skeleton with the loop bodies changed from `append` to assignment
- When a problem needs extra bookkeeping and forbids extra space, store the
  bookkeeping inside the grid. Set Matrix Zeroes uses row 0 as the list of
  columns to zero and column 0 as the list of rows to zero
  - Cell `(0, 0)` belongs to both marker regions and cannot hold two independent
    facts, so one of them moves into a separate boolean. On `[[1, 0], [1, 1]]`
    the version without that boolean returns `[[0, 0], [0, 0]]` instead of
    `[[0, 0], [1, 0]]`
  - Write the answer bottom to top and column 0 last, because the markers must
    stay readable until the rows that depend on them are finished
- When every cell has to be updated simultaneously, keep the current state in
  bit 0 and write the next state into bit 1 of the same cell, then finish with a
  pass of `>>= 1`
  - Every read of a neighbour must be masked with `& 1`, because that neighbour
    may already carry a `2` or a `3`, and the mask recovers the pre-pass state
  - Only survivals and births write anything, since `|= 2` sets bit 1 and a death
    means leaving bit 1 as the `0` it already is
- All four transforms are `O(R * C)` time, because each visits every cell a fixed
  number of times, and all four are `O(1)` auxiliary space, because the point of
  every one of them is to avoid the second grid the naive version allocates

## Interview Checklist

```text
Am I consistently writing matrix[row][column], with the row index first?
Is the matrix square, given that transpose-plus-reverse only rotates a square?
Does my transform write each cell straight to its destination, and if so, which
  value does the first write destroy?
For the transpose: does the inner loop start at r + 1 so each pair swaps once?
Clockwise or counterclockwise, and is that row.reverse() or matrix.reverse()?
For a spiral: are the bottom and left passes guarded, and did I test a single
  row and a single column?
For in-grid markers: which cell is being asked to mean two things, and which of
  those meanings moved into a variable?
For in-grid markers: does my write order destroy a marker another row still
  needs to read?
For simultaneous updates: is every neighbour read masked back to its old state?
Did I guard the empty matrix before calling len(matrix[0])?
Is the answer returned, or is it the mutation of the input?
What are R and C here, and is my bound O(R * C) or something worse?
```
