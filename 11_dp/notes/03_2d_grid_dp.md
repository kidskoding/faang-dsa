# 2D and Grid DP

A **2D DP** is a dynamic program whose state needs **two numbers to name it**
instead of one. In [1D DP](02_1d_dp.md) a subproblem was identified by a single
index, so the table was one row of values and a left-to-right loop filled it. Here
a subproblem is identified by a pair, so the table is a rectangle and each entry
`dp[r][c]` answers one question about the pair `(r, c)`

**Grid DP** is the case where that pair is a literal coordinate on a grid you were
handed. It is the easiest place to learn the shape, because the table has the same
dimensions as the input and you can point at the cells that feed a cell. The pair
does not have to be coordinates, and later topics use a pair of positions in two
strings or a pair of item index and remaining capacity, but the machinery is the
one below

The `dp` table is not the grid. The grid holds the input, such as a cost or a
`"1"`, while `dp[r][c]` holds an **answer** about that position, such as how many
ways there are to reach it or the cheapest total to arrive there. Keeping the two
apart in your head is most of the work

One thing genuinely changes when the state gains a second index. In one dimension
"everything before `i`" points in a single direction, so any left-to-right loop is
automatically a valid order. On a grid, a cell can depend on the cell above **and**
the cell to its left at the same time, and the loop order now has to satisfy both
dependencies at once. That constraint is the whole extra difficulty of two
dimensions

## Why Counting Paths One At A Time Dies

[Unique Paths](https://leetcode.com/problems/unique-paths/) puts a robot in the
top-left cell of an `m` by `n` grid. It may only move one cell right or one cell
down, and you must count the distinct ways it can reach the bottom-right cell

The direct solution is to count the paths by walking them. From a cell you either
go right or go down, so the number of paths from here is the number after moving
right plus the number after moving down. When you are stuck against the top row or
the left column there is only one route left, which is to go straight along it

```python
def count_paths_naive(m: int, n: int) -> int:
    if m == 1 or n == 1:
        return 1
    return count_paths_naive(m - 1, n) + count_paths_naive(m, n - 1)


assert count_paths_naive(3, 7) == 28
assert count_paths_naive(3, 2) == 3
assert count_paths_naive(1, 1) == 1
```

This is correct and it is unusable, because the recursion bottoms out exactly once
per path and the number of paths explodes. Every path is a sequence of `m + n - 2`
moves of which `m - 1` are downward, so there are `C(m + n - 2, m - 1)` of them. A
15 by 15 grid therefore has 40,116,600 paths, and instrumenting the function above
to count its own calls on that input reports 80,233,199 of them

Now compare that with the number of *questions* being asked. The grid has 225
cells, and the count from a cell onward never depends on how the robot got there,
since the remaining moves are the same either way. So the recursion is answering
225 distinct questions 80 million times

That is the concrete failure, and it hands you the fix. Give each cell one entry,
compute it once, and read it forever after. There are `m * n` states, which is
where the `O(m * n)` in every problem in this topic comes from

## What A Cell Is Allowed To Read

Flip the direction so the table is filled forwards, which is the more common
convention for grids and makes the base cases sit at the start

```text
dp[r][c] = the number of distinct paths from the start cell (0, 0) to cell (r, c)
```

The last move into `(r, c)` was either downward from `(r - 1, c)` or rightward from
`(r, c - 1)`. Those two groups of paths share no members, because a path has one
final move, and together they account for every path that arrives, because there
is no third way in. So the counts add

```text
              c-1        c
          +---------+---------+
   r-1    |         |    A    |
          +---------+----|----+
                     down |
          +---------+----v----+
   r      |    B ---+--> X    |
          +---------+ right---+

X = A + B
```

Both arrows point up and to the left, which is what decides the fill order. A
double loop with rows on the outside running top to bottom and columns on the
inside running left to right has already written `A` on the previous row pass and
`B` a moment ago on this one. That is the test to apply to any grid recurrence
before writing it: draw the arrows, and if every arrow points backward in your
loop order, the order is legal

The first row and the first column have no cell above or no cell to the left, so
they are the base cases. There is exactly one path along the top row, which is all
rights, and exactly one down the left column, which is all downs, so both are
filled with 1

```python
def unique_paths(m: int, n: int) -> int:
    dp = [[1] * n for _ in range(m)]
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
    return dp[m - 1][n - 1]


assert unique_paths(3, 7) == 28
assert unique_paths(3, 2) == 3
assert unique_paths(1, 1) == 1
assert unique_paths(1, 10) == 1
```

Initializing the whole table to 1 is what lets both loops start at index 1, since
the base row and column are already correct and the general recurrence never needs
to run on them. The finished table for `m = 3` and `n = 4` is Pascal's triangle
laid on its side:

```text
c ->     0    1    2    3
r=0      1    1    1    1
r=1      1    2    3    4
r=2      1    3    6   10
```

Cell `(2, 3)` holds 10, which is `6` from its left plus `4` from above

An alternative to writing the base row by hand is to **pad** the table with an
extra row and column of zeros, index the real grid from 1, seed `dp[0][1] = 1` so
the first real cell inherits a single path, and let the recurrence run everywhere
with no bounds checks. It is less code, and the trap is that the pad value has to
suit the combine: zeros are the identity for a sum, but for a minimum you must pad
with `float("inf")`, or the pad wins every comparison and the answer collapses to
the last cell's own value

## Blocked Cells Are Zero, Not Missing

[Unique Paths II](https://leetcode.com/problems/unique-paths-ii/) adds obstacles,
marked `1` in the input grid, that the robot cannot stand on. The recurrence does
not change at all. An obstacle simply has zero ways to be reached, and writing a
`0` there makes every cell downstream of it inherit that fact automatically,
because a zero contributes nothing to the sums it feeds

What does change is the base row and column, which is the part people get wrong.
You can no longer fill them with 1s in a blanket loop, since an obstacle anywhere
in the top row cuts off every cell after it. The cleanest fix is to stop special
casing the boundary and instead run one loop over every cell that adds a
contribution only when that neighbour exists

```python
def unique_paths_with_obstacles(obstacle_grid: list[list[int]]) -> int:
    m, n = len(obstacle_grid), len(obstacle_grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1 - obstacle_grid[0][0]
    for r in range(m):
        for c in range(n):
            if obstacle_grid[r][c] == 1:
                dp[r][c] = 0
                continue
            if r > 0:
                dp[r][c] += dp[r - 1][c]
            if c > 0:
                dp[r][c] += dp[r][c - 1]
    return dp[m - 1][n - 1]


assert unique_paths_with_obstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
assert unique_paths_with_obstacles([[0, 1], [0, 0]]) == 1
assert unique_paths_with_obstacles([[1]]) == 0
assert unique_paths_with_obstacles([[0]]) == 1
```

`dp[0][0] = 1 - obstacle_grid[0][0]` seeds the start with one path when it is
open and none when the start itself is blocked, which is the degenerate input
`[[1]]` that the last two asserts pin down. The `+=` on a cell that was seeded is
harmless, because `(0, 0)` has neither a cell above nor a cell to its left, so
neither guard fires

### Tracing The Obstacle Grid

Take a 3 by 3 grid with a single obstacle at `(0, 1)`, immediately right of the
start. Cells are visited in row-major order, and each line names what the cell read

```text
cell    grid   reads                       dp
(0,0)    0     seeded, no neighbours        1
(0,1)    1     OBSTACLE, forced to zero     0
(0,2)    0     left = 0                     0   <- reachable on paper, unreachable in fact
(1,0)    0     above = 1                    1
(1,1)    0     above = 0, left = 1          1
(1,2)    0     above = 0, left = 1          1
(2,0)    0     above = 1                    1
(2,1)    0     above = 1, left = 1          2
(2,2)    0     above = 1, left = 2          3
```

The discarded cell is `(0, 2)`. It holds no obstacle and it sits in the top row, so
the blanket "first row is all 1s" initialization would have given it a 1 and the
final answer would have come out as 4 instead of 3. The table correctly gives it a
0, because its only feeder is the obstacle beside it. A cell being open is not the
same statement as a cell being reachable, and only the table knows the difference

## The Same Table With A Different Combine

Swap the `+` for a `min` and the identical machinery solves
[Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/), where each
cell holds a cost and you want the cheapest route to the bottom-right corner

```text
dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])
```

The justification is the same two-case split as before. The cheapest route into
`(r, c)` ends with a move from above or a move from the left, and whichever
predecessor it came through, the cost of the route splits cleanly into the cost of
reaching that predecessor plus the cost of this cell. So taking the cheaper of the
two already-computed predecessors is safe, and no route that arrives some other way
exists

```python
def min_path_sum(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for c in range(1, n):
        dp[0][c] = dp[0][c - 1] + grid[0][c]
    for r in range(1, m):
        dp[r][0] = dp[r - 1][0] + grid[r][0]
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])
    return dp[m - 1][n - 1]


assert min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
assert min_path_sum([[1, 2, 3], [4, 5, 6]]) == 12
assert min_path_sum([[5]]) == 5
```

Here the base row and column must be **running totals** rather than a constant,
because there is only one route along them but it still costs something. On the
first example the table comes out as

```text
c ->     0    1    2
r=0      1    4    5
r=1      2    7    6
r=2      6    8    7
```

and the answer is the corner, 7, which is the route `1 -> 3 -> 1 -> 1 -> 1`

[Minimum Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum/)
changes two things and is worth doing because both changes recur. A falling path
starts anywhere in the top row, and each step moves down to the column directly
below or diagonally adjacent, so a cell has **three** predecessors rather than two,
all of them in the previous row. It may also end anywhere in the bottom row, so
the answer is the minimum over that whole row instead of one fixed corner

```python
def min_falling_path_sum(matrix: list[list[int]]) -> int:
    n = len(matrix)
    prev = matrix[0][:]
    for r in range(1, n):
        prev = [matrix[r][c] + min(prev[max(c - 1, 0) : c + 2]) for c in range(n)]
    return min(prev)


assert min_falling_path_sum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]) == 13
assert min_falling_path_sum([[-19, 57], [-40, -5]]) == -59
assert min_falling_path_sum([[7]]) == 7
```

`max(c - 1, 0)` clamps the left edge, and the slice's right end needs no clamp
because Python truncates a slice that runs past the end of a list. Since every read
is from the previous row only, one list is enough to carry the state forward, and
the rows evolve as

```text
[ 2,  1,  3]
[ 7,  6,  5]
[13, 13, 14]
```

The final `min(prev)` is 13. Reading the corner instead would have answered 14,
and forgetting that the ending column is free is the standard wrong answer on this
problem

## Where The Base Case Sits Decides Which Way You Fill

[Triangle](https://leetcode.com/problems/triangle/) gives a triangular array where
row `r` holds `r + 1` numbers, and from position `(r, c)` you may step to
`(r + 1, c)` or `(r + 1, c + 1)`. You want the cheapest total from the apex to the
bottom row

Filling this downward from the apex is possible and unpleasant, because the first
and last entry of every row have only one predecessor while the middle entries have
two, so the loop needs edge cases at both ends of every single row, and at the end
you still have to take a minimum over the bottom row

Turn it around. Define the state as the cost **from here down to the bottom**,
which makes the bottom row the base case, since a cell there costs exactly its own
value. Then every cell in row `r` has both of its successors in range, because row
`r + 1` is exactly one longer, so there is no boundary case anywhere

```text
dp[c] = triangle[r][c] + min(dp[c], dp[c + 1])
```

```python
def minimum_total(triangle: list[list[int]]) -> int:
    dp = triangle[-1][:]
    for r in range(len(triangle) - 2, -1, -1):
        for c in range(len(triangle[r])):
            dp[c] = triangle[r][c] + min(dp[c], dp[c + 1])
    return dp[0]


assert minimum_total([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
assert minimum_total([[-10]]) == -10
```

One list is reused across rows, and writing into it in place is safe here because
the write at index `c` only ever destroys a value that the remaining reads, which
are at indices `c + 1` and higher, no longer need. The prefix of the list that
matters shrinks by one each row until only `dp[0]` is left

```text
row 3    [ 4,  1,  8,  3]
row 2    [ 7,  6, 10]
row 1    [ 9, 10]
row 0    [11]
```

The general lesson generalizes past this problem. **The direction you fill is set
by where the base case is**, not by habit, and if a recurrence is producing edge
cases everywhere, try defining the state from the other end before writing more
code

## Keeping One Row Instead Of The Whole Table

Every recurrence so far reads only row `r - 1` and cells to the left on row `r`, so
the rows above `r - 1` are dead weight. Two rows always suffice, and sometimes one
does, which takes the space from `O(m * n)` down to `O(n)`

Unique Paths collapses to a single line

```python
def unique_paths_one_row(m: int, n: int) -> int:
    row = [1] * n
    for _ in range(m - 1):
        for c in range(1, n):
            row[c] += row[c - 1]
    return row[-1]


assert unique_paths_one_row(3, 7) == 28
assert unique_paths_one_row(3, 2) == 3
assert unique_paths_one_row(1, 1) == 1
assert unique_paths_one_row(1, 10) == 1
```

`row[c] += row[c - 1]` works because of exactly when each side is read. At that
moment `row[c]` has not been touched on this pass, so it still holds the previous
row's value, which is the cell **above**. Meanwhile `row[c - 1]` was written a
moment ago on this pass, so it holds the current row's value, which is the cell to
the **left**. Both are what the recurrence asked for, and the rows it produces are
the rows of the full table

```text
[1, 1, 1, 1]
[1, 2, 3, 4]
[1, 3, 6, 10]
```

That correctness is a coincidence of this recurrence, not a property of rolling
rows, and assuming it is the mistake that makes space-optimized DP unreliable.
Minimum Falling Path Sum reads `c - 1` from the **previous** row, and an in-place
row has already overwritten that slot with the current row's value:

```text
matrix = [[-2, 8],
          [ 9, 0]]

two rows, correct          row = [-2, 8] -> [7, -2]           answer -2
one row, in place          row = [-2, 8] -> [7, 8] -> [7, 7]  answer  7
```

The in-place version computes `row[1] = 0 + min(row[0], row[1])` after `row[0]` has
already become 7, so it never sees the `-2` that the real answer depends on. Both
numbers above are what the two versions actually print

The rule to carry away is that an in-place row is safe only when every leftward
read is one you wanted from the **current** row. When the recurrence needs a left
or diagonal neighbour from the previous row, either keep two lists, as the falling
path code above does by rebuilding `prev` each pass, or save the value into a
temporary variable before it is clobbered, which the worked example does next

## Worked Example: [Maximal Square](https://leetcode.com/problems/maximal-square/)

Given a matrix of `"0"` and `"1"` characters, find the largest square whose cells
are all `"1"`, and return its area

**Input**: `matrix`, a `list[list[str]]` with `m` rows and `n` columns, both at
least 1. Every entry is a single-character string that is either `"0"` or `"1"`,
not an integer, which is a detail worth reading twice because comparing against
`1` instead of `"1"` silently finds nothing

**Output**: an `int`, the **area** of the largest all-ones square, meaning the side
length squared. It is `0` when the matrix contains no `"1"` at all. Returning the
side length instead of the area is the most common way to fail this problem on the
first submission

The naive reading is to try every square directly. For each cell as a top-left
corner and each side length `k`, verify that all `k²` cells are ones and keep the
largest that passes. That is `O(m * n * min(m, n)³)`, because there are `m * n`
corners, up to `min(m, n)` side lengths per corner, and up to `min(m, n)²` cells to
check per square, and it does the same verification work over and over on
overlapping squares

The state-design move is the whole problem. "Is there a square of side `k`
somewhere" has no useful recurrence, because it is not attached to a position.
**Anchor the square to a cell** instead, and pick the bottom-right corner, since
that is the corner the row-major scan reaches last

```text
dp[r][c] = the side length of the largest all-ones square whose bottom-right
           corner is cell (r, c), and 0 when matrix[r][c] is "0"
```

Every square has exactly one bottom-right corner, so scanning all cells considers
every square exactly once and nothing is missed or double counted

Now the recurrence. Suppose the three neighbours above, left, and diagonally
up-left each anchor a square of side at least `s - 1`. Those three squares together
cover every cell of the `s` by `s` block anchored at `(r, c)` except `(r, c)`
itself, which is a `"1"` by assumption, so a square of side `s` fits here. Going
the other way, if a square of side `s` does end at `(r, c)`, then chopping off its
last row or last column leaves a square of side `s - 1` ending at each of those
three neighbours. So the largest side that fits is one more than the **smallest**
of the three, and the smallest is the bottleneck that stops the square growing

> "I will let `dp[r][c]` be the side of the biggest all-ones square whose
> bottom-right corner is this cell. If the cell is a one, that side is one plus the
> minimum of the three neighbours above, left, and up-left, because the smallest of
> them is what limits how far the square can extend back. I track the best side as
> I scan and square it at the end."

1. Allocate a `dp` table the same shape as the matrix, filled with zeros, and keep
   a running `best` side of 0. Zero is the right default because a cell holding
   `"0"` anchors no square at all, and leaving it as zero also makes it a correct
   blocker for the `min` in its neighbours
2. Scan the cells in row-major order, rows top to bottom and columns left to right,
   since all three cells the recurrence reads lie above or to the left and are
   therefore already final by the time you arrive
3. When the cell is `"0"`, leave its entry at zero and move on. This is the step
   that propagates the blocking, because any square that would have crossed this
   cell now sees a zero in its minimum
4. When the cell is `"1"` and it sits in the first row or the first column, set the
   entry to 1. A square anchored on an edge cannot extend past the edge, so 1 is
   the most that ever fits there, and this is also what keeps the recurrence from
   indexing off the table
5. Otherwise set the entry to `1 + min(above, left, up-left)`, which is the argument
   above turned into code. Using `min` and not `max` is the line to check twice,
   because a `max` compiles, runs, and reports squares that do not exist
6. Update `best` with the entry each time you write one, then return `best * best`
   at the end, converting the side you tracked into the area the problem asked for

```python
def maximal_square(matrix: list[list[str]]) -> int:
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    best = 0
    for r in range(m):
        for c in range(n):
            if matrix[r][c] == "1":
                if r == 0 or c == 0:
                    dp[r][c] = 1
                else:
                    dp[r][c] = 1 + min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1])
                best = max(best, dp[r][c])
    return best * best


assert (
    maximal_square(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
    )
    == 4
)
assert maximal_square([["0", "1"], ["1", "0"]]) == 1
assert maximal_square([["0"]]) == 0
```

- **Time Complexity:** `O(m * n)` for `m` rows and `n` columns, because each cell
  is written once and its value comes from a `min` over three neighbours, which is
  constant work
- **Space Complexity:** `O(m * n)` for the table as written, which drops to `O(n)`
  with the rolling row below, since a cell only ever reads the row above and the
  cell beside it

### Tracing The Squares

The `dp` table for the first example, printed by running the code above:

```text
input                       dp
1  0  1  0  0               1  0  1  0  0
1  0  1  1  1               1  0  1  1  1
1  1  1  1  1               1  1  1  2  2
1  0  0  1  0               1  0  0  1  0
```

Three cells explain the whole recurrence. At `(2, 2)` the matrix holds a `"1"` and
both the cell above and the cell to the left hold 1, so a 2 by 2 square looks
plausible, but the up-left neighbour `(1, 1)` is 0 because the input has a zero
there. The minimum is 0, the candidate side of 2 is **rejected**, and the cell
settles at 1, which is correct since the 2 by 2 block ending at `(2, 2)` contains
that zero

At `(2, 3)` all three neighbours are 1, so the entry becomes 2 and `best` rises to
2, giving the answer `2 * 2 = 4`. At `(3, 3)` the cell above holds 2 and the up-left
holds 1, but the left neighbour `(3, 2)` is 0, so the minimum is again 0 and the
entry drops back to 1. A single zero anywhere in the block is enough to stop the
square, and routing that fact through the `min` of three is exactly how the
recurrence enforces it

### Counting Squares Instead Of Measuring The Biggest

[Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)
asks how many all-ones squares the matrix contains, of any size, and needs the same
table with one line changed

If `dp[r][c]` is `s`, then squares of side `1, 2, ..., s` all end at that cell, each
one nested inside the next, and no square of side greater than `s` does. So that
cell anchors exactly `s` squares. Since every square has one bottom-right corner,
summing the whole table counts every square exactly once

```python
def count_squares(matrix: list[list[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    total = 0
    for r in range(m):
        for c in range(n):
            if matrix[r][c] == 1:
                if r == 0 or c == 0:
                    dp[r][c] = 1
                else:
                    dp[r][c] = 1 + min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1])
                total += dp[r][c]
    return total


assert count_squares([[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]) == 15
assert count_squares([[1, 0, 1], [1, 1, 0], [1, 1, 0]]) == 7
assert count_squares([[0]]) == 0
```

The entries here are integers rather than the character strings Maximal Square
uses, which is a difference in the two problem statements and not in the technique

### Rolling One Row Through The Diagonal

Maximal Square is the case the earlier warning was about. It reads `dp[r][c - 1]`
from the current row, which an in-place list holds correctly, but it also reads
`dp[r - 1][c - 1]` from the previous row, and that slot was overwritten one
iteration ago. Save it into a variable before the write and the whole table
collapses to one list

```python
def maximal_square_one_row(matrix: list[list[str]]) -> int:
    n = len(matrix[0])
    row = [0] * n
    best = 0
    for r in range(len(matrix)):
        prev_diag = 0
        for c in range(n):
            saved = row[c]
            if matrix[r][c] == "1":
                row[c] = 1 if r == 0 or c == 0 else 1 + min(row[c], row[c - 1], prev_diag)
                best = max(best, row[c])
            else:
                row[c] = 0
            prev_diag = saved
    return best * best


assert (
    maximal_square_one_row(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
    )
    == 4
)
assert maximal_square_one_row([["0", "1"], ["1", "0"]]) == 1
assert maximal_square_one_row([["0"]]) == 0
```

`saved` captures `row[c]`, which is the previous row's value at column `c`, before
anything overwrites it, and it becomes `prev_diag` for the next column, where it is
the previous row's value at column `c - 1`. `prev_diag` resets to 0 at the start of
each row because column 0 has no diagonal neighbour, and the `else: row[c] = 0`
branch is required rather than optional, since a stale value left over from the
previous row would otherwise be read as this row's answer

## Time and Space Complexity

Throughout, `m` is the number of rows and `n` is the number of columns

**Counting or costing paths through a grid, which is Unique Paths, Unique Paths II,
and Minimum Path Sum**

| Approach                   | Time                                                                                                                                                                           | Space                                                                                                                   |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| Full `dp` table, row-major | `O(m * n)`: there are `m * n` states and each one combines two already-final neighbours in constant time                                                                       | `O(m * n)`: one entry stored per cell, held for the whole run even though most of it is never read again                |
| One rolling row            | `O(m * n)`: the same cell count, since the space saving changes where values live and not how many are computed                                                                | `O(n)`: a single list the width of the grid, valid because a cell reads only the row above it and the cells to its left |
| Enumerating every path     | `O(C(m + n - 2, m - 1))`: the recursion bottoms out once per path, so on a 15 by 15 grid it makes 80,233,199 calls against 225 distinct states, which was measured by counting | `O(m + n)`: the call stack holds one partial path at a time, and a path is `m + n - 2` moves long                       |

**Largest and counted squares, which is Maximal Square and Count Square
Submatrices**

| Approach                        | Time                                                                                                                                          | Space                                                                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `1 + min` of three neighbours   | `O(m * n)`: one write per cell, and the `min` over three fixed neighbours is constant work                                                    | `O(m * n)` for the table, or `O(n)` for the rolling row that carries the diagonal in one extra variable              |
| Checking every candidate square | `O(m * n * min(m, n)³)`: `m * n` corners, up to `min(m, n)` side lengths each, and up to `min(m, n)²` cells verified per square with no reuse | `O(1)`: nothing is stored beyond the running best, which is exactly why it has to redo the overlapping verifications |

**Triangle and Minimum Falling Path Sum**, where `n` is the number of rows

| Approach                                    | Time                                                                                                                    | Space                                                                                                                     |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Triangle, bottom-up over one list           | `O(n²)`: row `r` holds `r + 1` cells, and `1 + 2 + ... + n` is `n(n + 1) / 2`, which is quadratic in the number of rows | `O(n)`: one list as wide as the bottom row, overwritten in place because each write destroys only values already consumed |
| Falling path, two rows over a square matrix | `O(n²)`: `n²` cells, each taking a `min` over three cells of the previous row                                           | `O(n)`: one previous row kept, rebuilt rather than overwritten because the recurrence needs the old left neighbour        |

## Summary

- A **2D DP** names each subproblem with a pair of numbers rather than one, so the
  table is a rectangle and `dp[r][c]` holds the answer for that pair. **Grid DP** is
  the case where the pair is a coordinate in a grid you were given, which makes the
  dependencies easy to draw and is why it is the place to learn the shape
  - The `dp` table is never the input grid. The grid holds a cost or a `"1"`, and
    the table holds an answer about that position, such as how many ways reach it
    or the cheapest total to arrive there
- The signal for grid DP is a problem asking to count routes, find the cheapest or
  most valuable route, or find the largest shape, where movement is restricted to
  one or two directions such as right and down. That restriction is what makes
  earlier cells final by the time you need them
  - When movement is unrestricted and you can step in all four directions, the
    dependencies form cycles and there is no valid fill order, so the problem is a
    graph search rather than a DP
- Walking every route individually costs one unit of work per route, and the number
  of routes through an `m` by `n` grid is `C(m + n - 2, m - 1)`, which is
  exponential. The table replaces that with one entry per cell, so the work drops to
  the `m * n` distinct questions the recursion was re-answering
- A grid recurrence combines the cases for the **last move into the cell**, and it
  is correct because those cases are disjoint and exhaustive. Counting problems add
  the predecessors, cost problems take the `min` or `max` of them, and everything
  else about the loop stays the same
- The fill order has to make every cell the recurrence reads already final. Draw the
  arrows from a cell to its predecessors, and a row-major double loop is valid
  exactly when all of them point up or to the left
  - Whether you fill from the top or from the bottom is decided by **where the base
    case sits**. Triangle is written bottom-up because the bottom row already knows
    its own answer, which removes the boundary case at both ends of every row
- The first row and first column are the base cases, because they have no cell above
  or none to the left. Fill them with 1 for path counting, with running totals for
  path costs, and never with a blanket loop when obstacles are involved, since an
  obstacle cuts off everything after it in its own row
  - The alternative is to pad the table with an extra row and column so the general
    recurrence runs everywhere with no bounds checks, and the trap there is that the
    pad must be `0` for a sum but `float("inf")` for a minimum
- Blocked cells are written as `0` rather than skipped, and that zero propagates
  correctly on its own, because a zero adds nothing to a sum and wins any `min` it
  takes part in
- Anchoring a shape to a cell is the state-design move behind Maximal Square, where
  `dp[r][c]` is the side of the largest all-ones square whose **bottom-right corner**
  is that cell, and the recurrence is `1 + min(above, left, up-left)`
  - The `min` is the point, since the smallest of the three neighbours is the
    bottleneck that stops the square growing, and a `max` there runs happily while
    reporting squares that do not exist
  - Because every square has exactly one bottom-right corner, and a cell holding `s`
    anchors one square of each side from 1 to `s`, summing the same table counts
    every all-ones square, which is Count Square Submatrices for free
- Space drops from `O(m * n)` to `O(n)` by keeping one or two rows, since a cell
  reads only the row above and cells to its left
  - An in-place single row is safe only when every leftward read is one you wanted
    from the **current** row. Unique Paths qualifies, so `row[c] += row[c - 1]` is
    correct, and Minimum Falling Path Sum does not, because it needs the previous
    row's `c - 1` after that slot has been overwritten
  - When a previous-row diagonal is needed, as in Maximal Square, save it into one
    variable before the write instead of abandoning the optimization
- The cost of every problem in this topic is `O(m * n)` time, because each of the
  `m * n` states is computed once from a constant number of neighbours, and `O(m * n)`
  space for the table or `O(n)` for a rolled row
  - Triangle is `O(n²)` in the number of rows rather than `O(m * n)`, because its
    rows have lengths `1, 2, ..., n` and those sum to `n(n + 1) / 2`

## Interview Checklist

Before writing code, make sure you can answer each of these

```text
What does dp[r][c] mean in one sentence: ways to reach the cell, best cost to reach it,
  or the size of a shape ending at it?
Which cells does dp[r][c] read, and do all of those arrows point up or to the left?
Is my loop order top-to-bottom and left-to-right, and is that enough for those arrows?
Where is the base case, and does that mean I should fill from the top or from the bottom?
How are the first row and first column initialized, and does an obstacle or a zero break
  that initialization?
Am I adding the predecessors because I am counting, or taking min/max because I am
  optimizing, and are those predecessor cases disjoint and exhaustive?
Is the answer the bottom-right corner, or a min/max over a whole row because the path
  may end anywhere?
Does my state need to be "ending exactly at this cell" rather than "somewhere in the
  grid so far"?
If I roll down to one row, does any read need the previous row's left or diagonal value,
  and have I saved it before overwriting?
What is the answer on the degenerate inputs: a 1 by 1 grid, a blocked start cell, and a
  matrix with no ones at all?
```
