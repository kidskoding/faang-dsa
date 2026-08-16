# Grid Backtracking

A grid is a decision tree wearing a disguise. Standing on a cell, the moves
available are the neighbours above, below, left, and right, so walking a grid is
the same choose-a-branch-then-recurse shape as
[building a permutation one slot at a time](03_permutations.md). The only thing
that changed is where the choices come from, since a permutation reads them out
of an array and a grid reads them off the board around you

What genuinely changes is **where the state lives**. In the earlier notes the
state was a `path` list that the recursion appended to and popped from, and
nothing outside that list remembered anything. Here the state is a mark written
into a structure that every branch shares: a cell blanked out on the board, a
column recorded as occupied, a running total added into a bucket. **Grid
backtracking** is the choose / explore / un-choose cycle from
[backtracking basics](01_backtracking_basics.md) applied to that shared state, so
the un-choose step stops being a `pop` and becomes "put the board back the way I
found it"

Think of walking a maze with chalk. You mark the floor as you enter a corridor so
you can tell you have already been there and don't circle forever, and when the
corridor dead-ends you rub the mark out on the way back, because that same
corridor may well be part of a route that starts somewhere else. Marking is what
makes the search terminate, and rubbing out is what makes it complete

This topic covers the mark-and-restore loop on a grid, boards where the conflict
is a shared column or diagonal rather than adjacency, searches that stop at the
first solution versus searches that count every one, undoing a move that is a
physical action rather than an assignment, and assigning a pile of values into
buckets

## Why A Cell Burned By A Failed Branch Stays Burned

Take [Word Search](https://leetcode.com/problems/word-search/): given a board of
letters and a word, decide whether the word can be spelled by stepping between
neighbouring cells without using any cell twice

Some kind of mark is obviously needed, because without one the walk can step off
a cell and immediately step back onto it, so the word `"AA"` would match a board
holding a single `A`. The natural first move is therefore a `visited` set that
the search adds to as it goes, which is the ordinary way to walk a structure
without repeating yourself

```python
DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))  # up, down, left, right


def exist_permanent_marks(board: list[list[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])
    visited: set[tuple[int, int]] = set()

    def dfs(r: int, c: int, i: int) -> bool:
        if i == len(word):
            return True
        if not (0 <= r < rows and 0 <= c < cols):
            return False
        if (r, c) in visited or board[r][c] != word[i]:
            return False
        visited.add((r, c))
        return any(dfs(r + dr, c + dc, i + 1) for dr, dc in DIRECTIONS)

    return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))


assert exist_permanent_marks([["A", "A", "A"], ["X", "X", "B"]], "AAB") is False
```

That assert is the bug. The word `AAB` is on that board, spelled by starting at
the middle `A`, stepping right to the third `A`, then down to the `B`. Here is
what the permanent set does instead. The search starts at `(0, 0)`, matches `A`,
steps right to `(0, 1)`, matches the second `A`, and then finds no `B` beside
`(0, 1)`, so that whole attempt fails. Both cells are still in `visited`. When
the outer loop reaches `(0, 1)` to try starting there, the very first check
rejects it as already seen, and the one route that spells the word is never
walked

The set is answering a different question. A permanent `visited` set is the right
tool for "which cells can I reach at all", where being reached once settles the
matter forever. This problem asks "is there **a path** that spells the word",
where a cell being unusable is a fact about one path, not a fact about the cell

That failure names the fix exactly. A mark has to be scoped to the branch that
made it, which means the mark comes off as the recursion returns

## Marking The Cell, Then Putting It Back

The undo has to run on every way out of the call, including the failing ones, so
the cleanest arrangement is to collect the four child results into one value
first and restore afterwards

```python
DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))  # up, down, left, right


def exist(board: list[list[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])

    def dfs(r: int, c: int, i: int) -> bool:
        if i == len(word):
            return True
        if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != word[i]:
            return False
        board[r][c] = "#"
        found = any(dfs(r + dr, c + dc, i + 1) for dr, dc in DIRECTIONS)
        board[r][c] = word[i]
        return found

    return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))


grid = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
assert exist(grid, "ABCCED") is True
assert exist(grid, "SEE") is True
assert exist(grid, "ABCB") is False
assert exist([["A", "A", "A"], ["X", "X", "B"]], "AAB") is True
assert exist([["a"]], "a") is True and exist([["a"]], "b") is False
assert grid == [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
```

**The three lines that are the whole technique** are `board[r][c] = "#"`, the
recursive fan-out, and `board[r][c] = word[i]`. Everything else is bookkeeping.
The restore sits on the single exit path shared by success and failure, which is
why it cannot be skipped; writing `return True` in the middle of the loop is how
people end up with a board that is still full of `#` when the next start cell is
tried

**The mark is written into the board rather than into a set.** Overwriting the
cell with `#` costs `O(1)` and no extra memory, and the equality test
`board[r][c] != word[i]` then doubles as the visited check for free, because `#`
is not a letter and can never match the character being looked for. Restoring
writes back `word[i]` rather than a remembered variable, which is safe precisely
because the function already proved `board[r][c] == word[i]` two lines above

**Mutating the input is a choice to say out loud.** It is fine when the board is
put back exactly as it was, which the last assert checks. Use a `visited` set
instead when the caller is not allowed to see the board change even briefly,
when the cell values have no spare sentinel to borrow, or when there is no board
to write to at all, which is the situation in Robot Room Cleaner further down.
When the grid holds numbers rather than characters, save the value first and put
that back, as the counting version below does

**The base case is checked before the bounds check, and the order matters.** By
the time `i == len(word)` the previous call already matched the final character,
so this call exists only to confirm that the word ran out. If the bounds test ran
first, a word whose last letter sits on the border of the board would be rejected
by a step that walks off the edge, and the search would report a false negative
for a word it had actually just finished spelling

**`any` over the four directions short-circuits**, so the moment one neighbour
reports success the remaining directions are never explored, and the argument is
a generator rather than a list so the calls happen lazily

**The outer `any` restarts the whole search from every cell**, since the word may
begin anywhere. Each of those searches begins with a clean board, which is only
true because the previous one restored everything it touched

> "I will mark the current cell with a sentinel before recursing so the path
> cannot reuse it, and put the letter back before returning so a different path
> can. The visited state belongs to the path, not to the board"

## Dry Run: Spelling "AAB" On A Two-Row Board

The board is the one that broke the permanent set, and the direction order is up,
down, left, right

```text
index   0    1    2
row 0   A    A    A
row 1   X    X    B
```

```text
START at (0,0)
  (0,0)='A' matches word[0], mark
    up      (-1,0) out of bounds          reject
    down    (1,0)='X' != 'A'              reject
    left    (0,-1) out of bounds          reject
    right   (0,1)='A' matches word[1], mark
      up    (-1,1) out of bounds          reject
      down  (1,1)='X' != 'B'              reject
      left  (0,0)='#' != 'B'              reject
      right (0,2)='A' != 'B'              reject
    (0,1) exhausted, unmark, return False
  (0,0) exhausted, unmark, return False
START at (0,1)
  (0,1)='A' matches word[0], mark
    up      (-1,1) out of bounds          reject
    down    (1,1)='X' != 'A'              reject
    left    (0,0)='A' matches word[1], mark
      up    (-1,0) out of bounds          reject
      down  (1,0)='X' != 'B'              reject
      left  (0,-1) out of bounds          reject
      right (0,1)='#' != 'B'              reject
    (0,0) exhausted, unmark, return False
    right   (0,2)='A' matches word[1], mark
      up    (-1,2) out of bounds          reject
      down  (1,2)='B' matches word[2], mark
        up  i == 3 == len(word)           return True
```

Two discarded steps carry the lesson. The first is the entire `START at (0,0)`
block, which explores, fails, and unmarks both cells, and it is the block whose
leftover marks killed the permanent-set version. The second is the step where the
search starting at `(0, 1)` goes left into `(0, 0)`, spends a level there, fails,
and unmarks it again, which is the same cell being borrowed and released twice
inside one run

The `left` rejections show the sentinel doing the visited check. At `(0,1)` the
cell to the left reads `#` rather than `A`, so the ordinary character comparison
rejects it without any separate membership test

The last line is worth pausing on. The base case fires on the call for `(0, 2)`,
a cell that is in bounds but currently marked `#`, so the character test below it
would have rejected the cell — and that test could not even run, because `word[3]`
is past the end of the word. `i == len(word)` runs first, which is why the call
reports success without ever looking at where it landed

## Stopping At The First Solution Versus Counting Every One

Word Search returns a `bool`, and that shapes the code beyond the return type.
The `any` unwinds the entire stack the instant something succeeds, so the branches
to the right of the winner are never explored and their undo lines never run. That
is exactly what you want when one witness settles the question

[Unique Paths III](https://leetcode.com/problems/unique-paths-iii/) asks the
opposite: walk from the start square to the end square covering every walkable
cell exactly once, and report **how many** such walks exist. A search that counts
cannot short-circuit, because every branch contributes

```python
DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))


def unique_paths_iii(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    start = (0, 0)
    walkable = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                walkable += 1
            elif grid[r][c] == 1:
                start = (r, c)
                walkable += 1

    def walk(r: int, c: int, left: int) -> int:
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == -1:
            return 0
        if grid[r][c] == 2:
            return 1 if left == 0 else 0
        original = grid[r][c]
        grid[r][c] = -1
        total = sum(walk(r + dr, c + dc, left - 1) for dr, dc in DIRECTIONS)
        grid[r][c] = original
        return total

    return walk(start[0], start[1], walkable)


assert unique_paths_iii([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]) == 2
assert unique_paths_iii([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]) == 4
assert unique_paths_iii([[0, 1], [2, 0]]) == 0
assert unique_paths_iii([[1, 2]]) == 1
```

Three things differ from the boolean version and all three follow from counting
rather than deciding. `any` becomes `sum`, so every direction is explored instead
of stopping at the first that works. The obstacle value `-1` is reused as the
visited sentinel, and the original cell value is saved and restored rather than
recomputed, because a cell can hold either `0` or the `1` marking the start.
Finally the recursion carries `left`, the number of walkable cells not yet
stepped on, and the end square only scores when `left == 0`, which is how "covers
every square" gets checked in `O(1)` at the leaf rather than by re-scanning the
grid

## Filling A Board Under Row, Column, And Box Rules

[Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) is the boolean shape
again, but the thing being marked is no longer the cell you are standing on. A
digit written at `(r, c)` constrains its row, its column, and its 3×3 box, so
three separate memberships have to be recorded and three have to be undone

Rather than scanning for the next blank on every call, collect the blanks once
into a list and let the recursion index into it, which turns "where do I go next"
into a plain integer and makes the base case a length comparison

```python
def solve_sudoku(board: list[list[str]]) -> None:
    rows: list[set[str]] = [set() for _ in range(9)]
    cols: list[set[str]] = [set() for _ in range(9)]
    boxes: list[set[str]] = [set() for _ in range(9)]
    blanks: list[tuple[int, int]] = []
    for r in range(9):
        for c in range(9):
            value = board[r][c]
            if value == ".":
                blanks.append((r, c))
            else:
                rows[r].add(value)
                cols[c].add(value)
                boxes[(r // 3) * 3 + c // 3].add(value)

    def fill(k: int) -> bool:
        if k == len(blanks):
            return True
        r, c = blanks[k]
        b = (r // 3) * 3 + c // 3
        for value in "123456789":
            if value in rows[r] or value in cols[c] or value in boxes[b]:
                continue
            board[r][c] = value
            rows[r].add(value)
            cols[c].add(value)
            boxes[b].add(value)
            if fill(k + 1):
                return True
            board[r][c] = "."
            rows[r].remove(value)
            cols[c].remove(value)
            boxes[b].remove(value)
        return False

    fill(0)


puzzle = [
    list("53..7...."),
    list("6..195..."),
    list(".98....6."),
    list("8...6...3"),
    list("4..8.3..1"),
    list("7...2...6"),
    list(".6....28."),
    list("...419..5"),
    list("....8..79"),
]
solve_sudoku(puzzle)
digits = set("123456789")
assert ["".join(row) for row in puzzle][0] == "534678912"
assert all(set(row) == digits for row in puzzle)
assert all({puzzle[r][c] for r in range(9)} == digits for c in range(9))


def box(br: int, bc: int) -> set[str]:
    return {puzzle[r][c] for r in range(br, br + 3) for c in range(bc, bc + 3)}


assert all(box(br, bc) == digits for br in (0, 3, 6) for bc in (0, 3, 6))

one_blank = [row[:] for row in puzzle]
one_blank[0][0] = "."
solve_sudoku(one_blank)
assert one_blank == puzzle

no_blanks = [row[:] for row in puzzle]
solve_sudoku(no_blanks)
assert no_blanks == puzzle
```

`(r // 3) * 3 + c // 3` numbers the boxes 0 to 8 in reading order, because
`r // 3` picks the band of three rows and `c // 3` picks the stack of three
columns, so multiplying the band by three and adding the stack gives each box a
distinct index

**The undo block is four lines and skipping any one of them is a different bug.**
Leaving the digit on the board makes a later branch read a value the constraint
sets no longer know about, and leaving a set entry behind falsely blocks a digit
that is actually available, which usually shows up as a solvable puzzle reported
unsolvable

**The `return True` deliberately skips the undo.** Once the last blank is filled
the board is the answer, so every frame on the way out returns immediately and
leaves its digit in place. Sudoku Solver is specified to mutate `board` rather
than return anything, so this is not laziness; the half-unwound state is the
deliverable. That is only ever safe in a search that stops at the first solution

## Conflicts That Are Not Adjacency

[N-Queens](https://leetcode.com/problems/n-queens/) places `n` queens on an
`n × n` board so that no two share a row, a column, or a diagonal. Nothing about
this is about neighbouring cells, and yet it is the same loop, because the shared
state being marked and unmarked is simply a different set of resources

The first reduction removes most of the search before it starts. Two queens can
never share a row, so any valid board has exactly one queen per row, which means
the recursion can go one row deep at a time and only decide **which column**.
That collapses the choice at each level from "any of the remaining cells" to
"one of `n` columns"

Diagonals need a key that is constant along the diagonal. Writing `r - c` and
`r + c` at every square of a 4×4 board shows what to use

```text
r - c                          r + c
   0  -1  -2  -3                0   1   2   3
   1   0  -1  -2                1   2   3   4
   2   1   0  -1                2   3   4   5
   3   2   1   0                3   4   5   6
```

Stepping down-right adds one to both `r` and `c`, so `r - c` does not change and
every square on a ↘ diagonal shares that value. Stepping down-left adds one to
`r` and subtracts one from `c`, so `r + c` does not change along a ↙ diagonal.
Three sets of integers therefore capture every conflict a queen can create

```python
def solve_n_queens(n: int) -> list[list[str]]:
    cols: set[int] = set()
    diagonals: set[int] = set()
    anti_diagonals: set[int] = set()
    queen_col: list[int] = []
    out: list[list[str]] = []

    def place(r: int) -> None:
        if r == n:
            out.append(["." * c + "Q" + "." * (n - c - 1) for c in queen_col])
            return
        for c in range(n):
            if c in cols or (r - c) in diagonals or (r + c) in anti_diagonals:
                continue
            cols.add(c)
            diagonals.add(r - c)
            anti_diagonals.add(r + c)
            queen_col.append(c)
            place(r + 1)
            queen_col.pop()
            cols.remove(c)
            diagonals.remove(r - c)
            anti_diagonals.remove(r + c)

    place(0)
    return out


assert solve_n_queens(4) == [
    [".Q..", "...Q", "Q...", "..Q."],
    ["..Q.", "Q...", "...Q", ".Q.."],
]
assert solve_n_queens(1) == [["Q"]]
assert solve_n_queens(2) == [] and solve_n_queens(3) == []
assert [len(solve_n_queens(k)) for k in range(1, 9)] == [1, 0, 0, 2, 10, 4, 40, 92]
```

`queen_col` holds one column index per placed row, so a full solution is `n`
integers and the board strings are built once at the leaf rather than carried
down the recursion. That is why no `[:]` copy appears here even though earlier
notes always copied the path: the list comprehension already builds a fresh list
of fresh strings, so nothing aliases the mutable `queen_col`

[N-Queens II](https://leetcode.com/problems/n-queens-ii/) wants only the number of
solutions, and the change is the one from the previous section. Delete
`queen_col` and the string building, return `1` at `r == n`, and add up the
children instead of appending to a list

```python
def total_n_queens(n: int) -> int:
    cols: set[int] = set()
    diagonals: set[int] = set()
    anti_diagonals: set[int] = set()

    def place(r: int) -> int:
        if r == n:
            return 1
        found = 0
        for c in range(n):
            if c in cols or (r - c) in diagonals or (r + c) in anti_diagonals:
                continue
            cols.add(c)
            diagonals.add(r - c)
            anti_diagonals.add(r + c)
            found += place(r + 1)
            cols.remove(c)
            diagonals.remove(r - c)
            anti_diagonals.remove(r + c)
        return found

    return place(0)


assert [total_n_queens(k) for k in range(1, 10)] == [1, 0, 0, 2, 10, 4, 40, 92, 352]
assert total_n_queens(1) == 1
```

> "A queen owns a row, a column, and two diagonals. I will place one queen per
> row so rows take care of themselves, and keep three sets keyed by column,
> `r - c`, and `r + c`. Adding to the three sets is the choice and removing from
> them is the undo"

## When The Undo Is A Move, Not An Assignment

[Robot Room Cleaner](https://leetcode.com/problems/robot-room-cleaner/) removes
the board entirely. You control a robot through four methods and never learn
where it is, what the room looks like, or how big it is. `move()` steps one cell
forward and returns `False` without moving when a wall is in the way, `turn_left`
and `turn_right` rotate ninety degrees, and `clean()` cleans the current cell

Two adjustments make this the same search. Coordinates are invented rather than
given, so call the starting cell `(0, 0)` and track offsets from it, which is
enough because only *relative* position is needed to tell one cell from another.
More importantly, the un-choose step cannot be an assignment. Undoing a move
means driving the robot back, and the sequence is turn around, move one cell,
turn around again so the heading is restored as well as the position

```python
HEADINGS = ((-1, 0), (0, 1), (1, 0), (0, -1))  # up, right, down, left


def clean_room(robot: "SimRobot") -> None:
    visited: set[tuple[int, int]] = set()

    def step_back() -> None:
        robot.turn_right()
        robot.turn_right()
        robot.move()
        robot.turn_right()
        robot.turn_right()

    def walk(r: int, c: int, h: int) -> None:
        visited.add((r, c))
        robot.clean()
        for turn in range(4):
            heading = (h + turn) % 4
            dr, dc = HEADINGS[heading]
            nr, nc = r + dr, c + dc
            if (nr, nc) not in visited and robot.move():
                walk(nr, nc, heading)
                step_back()
            robot.turn_right()

    walk(0, 0, 0)


class SimRobot:  # stands in for the hidden robot so the code can be run
    def __init__(self, room: list[list[int]], r: int, c: int) -> None:
        self.room, self.r, self.c, self.h = room, r, c, 0
        self.cleaned: set[tuple[int, int]] = set()

    def move(self) -> bool:
        dr, dc = HEADINGS[self.h]
        nr, nc = self.r + dr, self.c + dc
        inside = 0 <= nr < len(self.room) and 0 <= nc < len(self.room[0])
        if inside and self.room[nr][nc] == 1:
            self.r, self.c = nr, nc
            return True
        return False

    def turn_left(self) -> None:
        self.h = (self.h - 1) % 4

    def turn_right(self) -> None:
        self.h = (self.h + 1) % 4

    def clean(self) -> None:
        self.cleaned.add((self.r, self.c))


room = [
    [1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
]
bot = SimRobot(room, 1, 3)
clean_room(bot)
open_cells = {(r, c) for r in range(5) for c in range(8) if room[r][c] == 1}
assert bot.cleaned == open_cells and len(open_cells) == 30
assert (bot.r, bot.c, bot.h) == (1, 3, 0)

single = SimRobot([[1]], 0, 0)
clean_room(single)
assert single.cleaned == {(0, 0)} and (single.r, single.c, single.h) == (0, 0, 0)
```

**`robot.move()` is both the test and the action.** There is no way to ask
whether a wall is ahead without trying to drive into it, so the guard has to be
written as `(nr, nc) not in visited and robot.move()`, with the cheap membership
test first so a cell already handled is skipped without spending a move

**`robot.turn_right()` at the bottom of the loop runs on every iteration**,
including the ones where the move was refused, which is what keeps the loop
variable `turn` and the robot's real heading in step. After four iterations the
robot has turned a full circle and faces the direction it arrived in, which is
the assumption `step_back` in the parent frame is relying on. The last assert
checks exactly this by confirming the robot ends where it began, facing the same
way

**The `visited` set is never unmarked**, and that is not a contradiction of
everything above. This problem is "reach every cell", which is the reachability
question the permanent set was built for, so a cell handled once is handled
forever. What backtracks here is the robot, not the marking

## What Else Counts As A Board

The remaining problems in this section keep the mark-and-restore loop and change
what is being marked, so the shape transfers directly

- [24 Game](https://leetcode.com/problems/24-game/) makes the state a multiset of
  numbers. A choice picks two of them and an operator, and the un-choose puts the
  two operands back and removes the result, shrinking four numbers to three to
  two to one
- [Expression Add Operators](https://leetcode.com/problems/expression-add-operators/)
  carries the running value **and** the last operand down the recursion, since
  undoing multiplication precedence means subtracting the previous operand and
  re-adding it multiplied
- [Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/)
  counts the minimum removals first so the recursion has a fixed budget, then
  skips repeated characters at the same depth the way
  [duplicate values are skipped in combinations](02_subsets_combinations.md)
- [Word Break II](https://leetcode.com/problems/word-break-ii/) memoizes on the
  remaining suffix. A suffix that produced no sentence will produce none the next
  time it is reached, so caching the result turns repeated dead ends into a
  dictionary lookup. That is the one addition here that changes the complexity
  rather than the state

## Worked Example: [Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)

Given a list of positive integers and a number `k`, decide whether the values can
be split into exactly `k` groups whose sums are all the same. There is no grid,
and yet the board is `k` running totals that get added to and subtracted from

**Input**: `nums`, a `list[int]` of positive integers with
`1 <= len(nums) <= 16` and `1 <= nums[i] <= 10^4`, and `k`, an `int` with
`1 <= k <= len(nums)` giving how many groups to build

**Output**: a `bool` that is `True` exactly when such a split exists. Every value
has to be used and each one lands in exactly one group, and the groups are
unordered, so a split is the same split when the groups are relabelled

**The approach.** "Split into `k` subsets of equal sum" is a bucket assignment,
where the item being chosen at each level is a value from `nums` and the choice
being made is which bucket it goes in. The naive reading of that is to generate
all `k^n` assignments and check the sums at the end, and the specific waste is
that a branch whose first bucket has already overshot the target keeps being
extended for another `n - 1` levels before anything notices. Since every value is
positive, a bucket total never comes back down, so a bucket that has passed the
target is dead immediately and the check belongs on the way down

Two more cuts come free. Because the groups are unordered, empty buckets are
interchangeable, so a value that fails in the first empty bucket fails in every
other empty bucket and only one of them is worth trying. And because a large
value fits in fewer places than a small one, placing the largest first makes a
doomed branch fail near the root rather than after `n` levels of work

> "Each subset has to sum to `total // k`, so if `total` is not divisible by `k`
> there is no answer. I will assign values to buckets one at a time, refusing any
> placement that pushes a bucket past the target, and I will only try the first
> empty bucket because the others are identical to it"

Therefore,

1. Reject immediately when `sum(nums) % k` is non-zero, because `k` equal integer
   sums must divide the total exactly, and otherwise set `target = sum(nums) // k`
2. Sort `nums` descending, which is a pruning decision rather than a correctness
   one, since the answer does not depend on the order values are considered in.
   The largest values are the ones with the fewest legal homes, so deciding them
   first is what puts the failures near the root
3. Reject when the largest value exceeds `target`, since a value that cannot fit
   in an empty bucket cannot fit anywhere, and this also guarantees every later
   value fits somewhere
4. Keep `buckets`, a list of `k` running totals starting at zero. This is the
   board, and the choose / un-choose pair is `buckets[b] += nums[i]` matched by
   `buckets[b] -= nums[i]`
5. Recurse on `i`, the index of the value being placed, so the base case is
   `i == len(nums)`. Reaching it means every value found a home without any
   bucket exceeding `target`, and since the totals sum to `k * target` and none
   exceeds `target`, they must all equal `target`
6. At each level loop over the buckets and skip any where `buckets[b] + nums[i]`
   would exceed `target`, which is the pruning that makes the search finish
7. After a failed attempt in bucket `b`, break out of the loop if `buckets[b]` is
   zero. That bucket was empty when the value went in, and every empty bucket
   after it is indistinguishable, so all of them would fail the same way
8. Return `True` the moment a child call succeeds, since one valid split answers
   the question and the buckets do not need restoring on the way out

```python
def can_partition_k_subsets(nums: list[int], k: int) -> bool:
    total = sum(nums)
    if total % k:
        return False
    target = total // k
    nums = sorted(nums, reverse=True)
    if nums[0] > target:
        return False
    buckets = [0] * k

    def place(i: int) -> bool:
        if i == len(nums):
            return True
        for b in range(k):
            if buckets[b] + nums[i] <= target:
                buckets[b] += nums[i]
                if place(i + 1):
                    return True
                buckets[b] -= nums[i]
            if buckets[b] == 0:
                break
        return False

    return place(0)


assert can_partition_k_subsets([4, 3, 2, 3, 5, 2, 1], 4) is True
assert can_partition_k_subsets([1, 2, 3, 4], 3) is False
assert can_partition_k_subsets([2, 2, 2, 2, 3, 3, 7], 3) is True
assert can_partition_k_subsets([1, 1, 1, 1, 4, 4, 4, 5], 3) is False
assert can_partition_k_subsets([1], 1) is True
assert can_partition_k_subsets([1, 1], 3) is False
```

[Matchsticks to Square](https://leetcode.com/problems/matchsticks-to-square/) is
this function with `k` fixed at four and a length check, since four sides of equal
length is four subsets of equal sum

Tracing `[2, 2, 2, 2, 3, 3, 7]` with `k = 3` shows the undo earning its place. The
values sort to `[7, 3, 3, 2, 2, 2, 2]` and the target is `21 // 3 = 7`

```text
7 -> bucket 0                            buckets=[7, 0, 0]
  3 will not fit bucket 0 (7+3 > 7)
  3 -> bucket 1                          buckets=[7, 3, 0]
    3 will not fit bucket 0 (7+3 > 7)
    3 -> bucket 1                        buckets=[7, 6, 0]
      2 will not fit bucket 0 (7+2 > 7)
      2 will not fit bucket 1 (6+2 > 7)
      2 -> bucket 2                      buckets=[7, 6, 2]
        2 will not fit bucket 0 (7+2 > 7)
        2 will not fit bucket 1 (6+2 > 7)
        2 -> bucket 2                    buckets=[7, 6, 4]
          2 will not fit bucket 0 (7+2 > 7)
          2 will not fit bucket 1 (6+2 > 7)
          2 -> bucket 2                  buckets=[7, 6, 6]
            2 will not fit bucket 0 (7+2 > 7)
            2 will not fit bucket 1 (6+2 > 7)
            2 will not fit bucket 2 (6+2 > 7)
          undo 2 from bucket 2           buckets=[7, 6, 4]
        undo 2 from bucket 2             buckets=[7, 6, 2]
      undo 2 from bucket 2               buckets=[7, 6, 0]
      bucket 2 empty and failed -> break
    undo 3 from bucket 1                 buckets=[7, 3, 0]
    3 -> bucket 2                        buckets=[7, 3, 3]
      2 will not fit bucket 0 (7+2 > 7)
      2 -> bucket 1                      buckets=[7, 5, 3]
        2 will not fit bucket 0 (7+2 > 7)
        2 -> bucket 1                    buckets=[7, 7, 3]
          2 will not fit bucket 0 (7+2 > 7)
          2 will not fit bucket 1 (7+2 > 7)
          2 -> bucket 2                  buckets=[7, 7, 5]
            2 will not fit bucket 0 (7+2 > 7)
            2 will not fit bucket 1 (7+2 > 7)
            2 -> bucket 2                buckets=[7, 7, 7]
              every value placed -> True
```

The discarded work is the block that puts both threes into bucket 1. It reaches
`[7, 6, 0]`, spends three levels stuffing twos into bucket 2, and dies because
`6 + 2` overshoots seven. Three `undo` lines walk that back, and they are what
makes the next attempt legal, since bucket 1 has to be down to `3` again before
the second three can go into bucket 2 instead

The `break` in that run happens to fire on the last bucket, where the loop was
about to end anyway. Its value shows up on inputs that fail. Here is
`[1, 1, 1, 1, 4, 4, 4, 5]` with `k = 3`, which sorts to `[5, 4, 4, 4, 1, 1, 1, 1]`
against a target of `21 // 3 = 7`

```text
5 -> bucket 0                            buckets=[5, 0, 0]
  4 will not fit bucket 0 (5+4 > 7)
  4 -> bucket 1                          buckets=[5, 4, 0]
    4 will not fit bucket 0 (5+4 > 7)
    4 will not fit bucket 1 (4+4 > 7)
    4 -> bucket 2                        buckets=[5, 4, 4]
      4 will not fit bucket 0 (5+4 > 7)
      4 will not fit bucket 1 (4+4 > 7)
      4 will not fit bucket 2 (4+4 > 7)
    undo 4 from bucket 2                 buckets=[5, 4, 0]
    bucket 2 empty and failed -> break
  undo 4 from bucket 1                   buckets=[5, 0, 0]
  bucket 1 empty and failed -> break, bucket 2 is identical to it
undo 5 from bucket 0                     buckets=[0, 0, 0]
bucket 0 empty and failed -> break, buckets 1 and 2 are identical to it
result: False
```

The whole search dies after placing four values. The middle `break` refuses to
move the `4` sitting in bucket 1 over to bucket 2, because bucket 1 was empty when
that `4` went in and bucket 2 is empty too, so the subtree would come out
identical. The last
`break` does the same thing for the `5` at the root and kills two thirds of the
tree in one line. Without the cut, every one of those branches gets rebuilt and
rejected on its own

- **Time Complexity:** `O(n log n + k^n)` where `n` is `len(nums)`, because the
  sort dominates the setup and each of the `n` values considers up to `k` buckets
  in the worst case. The target check, the descending sort, and the empty-bucket
  break all remove branches, so the tree explored is far smaller than `k^n`,
  though none of them improve the worst-case bound
- **Space Complexity:** `O(n + k)`, because the recursion is one frame per value
  for `O(n)` stack depth, `buckets` holds `k` integers, and the sorted copy of
  `nums` is another `O(n)`

## Time and Space Complexity

`R` and `C` are the number of rows and columns of a grid, `L` is `len(word)`, and
`n` is the side of the N-Queens board. Recursion-stack space is counted and output
space is not

**Word Search**

| Approach                | Time                                                                                                                                                                               | Space                                                                                                                      |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Mark and restore        | `O(R · C · 3^L)`: each of the `R · C` cells starts its own search, and after the first step only 3 neighbours are worth trying because the fourth is the marked cell you came from | `O(L)`: one recursion frame per matched character, and the marking is written into the board so nothing else is allocated  |
| Permanent visited marks | `O(R · C)`: every cell is entered at most once across the whole search, which is exactly why it is too cheap to be answering this question                                         | `O(R · C)`: one entry per cell in the visited set, and it returns wrong answers, so the saving is not a trade worth making |

**Board and placement searches**

| Problem            | Time                                                                                                                                                                                | Space                                                                                                                         |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| N-Queens           | `O(n!)` node visits, because row `r` has at most `n - r` columns still free and multiplying those across the rows gives `n!`, plus `O(n²)` per solution to render the board strings | `O(n)`: three sets holding at most `n` keys each, `queen_col` with one entry per row, and `n` recursion frames                |
| N-Queens II        | `O(n!)`: the identical search, since counting removes the board building but not a single node of the tree                                                                          | `O(n)`: the three sets and the recursion, with no `queen_col` and no output list                                              |
| Sudoku Solver      | `O(9^b)` where `b` is the number of blanks, because each blank tries up to 9 digits and every one that conflicts is rejected without recursing                                      | `O(b)`: one recursion frame per blank, since the 27 constraint sets hold at most 81 entries between them, which is a constant |
| Unique Paths III   | `O(3^(R · C))`: the walk can cover every cell and has 3 onward choices after the first step, and no branch can be cut short because every path has to be counted                    | `O(R · C)`: the recursion can be as deep as the number of walkable cells, and the marking is written into the grid            |
| Robot Room Cleaner | `O(R · C)` calls and `O(R · C)` robot moves, because each cell is walked into once and each entry is paid back by exactly one `step_back`                                           | `O(R · C)`: the `visited` set holds every reachable cell, and the recursion can be that deep on a snake-shaped room           |

## Summary

- **Grid backtracking** walks a grid as a decision tree, where the choices at each
  cell are its up-to-four neighbours and the recursion depth is the length of the
  path so far. It is the same choose / explore / un-choose loop as subsets and
  permutations, with the state living in the shared board instead of in a `path`
  list
  - The signal is a problem asking for a path, a placement, or an assignment
    where one attempt failing does not make the resource permanently unusable
- The mistake that defines the topic is a `visited` set that is never unmarked. A
  permanent set answers "which cells can I reach", where being visited once is
  final, while these problems ask "is there a path", where a cell is blocked for
  one route and free for another
  - Concretely, on `[["A","A","A"], ["X","X","B"]]` searching for `"AAB"`, the
    failed attempt from `(0, 0)` leaves the middle `A` marked, and the middle `A`
    is where the only real answer starts
- Writing the sentinel `#` into the cell is cheaper than a set and doubles as the
  visited check, because the character comparison that tests the next letter
  rejects `#` automatically. Restore the original value on the way out, and put
  the restore on the single exit path so it runs after failure as well as success
  - Say out loud that the input is being mutated and that it is put back exactly
    as found, since interviewers ask
- A search that returns a `bool` stops at the first solution, so `any` or
  `if child(): return True` short-circuits and the undo lines on the winning path
  never run. Sudoku Solver depends on that, because the half-unwound board is the
  answer it is supposed to leave behind
  - A search that counts, like Unique Paths III and N-Queens II, replaces `any`
    with `sum` and can never short-circuit, so every branch is explored and every
    undo runs
- Board problems mark occupied resources rather than cells. N-Queens places one
  queen per row and keeps three sets keyed by column, `r - c`, and `r + c`,
  because `r - c` is constant along a ↘ diagonal and `r + c` is constant along a
  ↙ one. Adding three keys is the choice and removing all three is the undo
- Robot Room Cleaner is the case where undo is an action rather than an
  assignment. Backing out is turn right twice, move, turn right twice, which
  restores heading as well as position, and the loop turns once per iteration so
  four iterations leave the robot facing the way it arrived
  - Its `visited` set is genuinely permanent, because "clean every cell" really is
    a reachability question, and what backtracks is the robot rather than the mark
- Bucket assignment is the same loop over `k` running totals. Partition to K Equal
  Sum Subsets rejects when `sum(nums) % k` is non-zero, refuses any placement that
  pushes a bucket past `sum(nums) // k`, sorts descending so hard values fail
  early, and breaks out after failing in an empty bucket because all empty buckets
  are interchangeable
  - Matchsticks to Square is the same function with `k` fixed at four

## Interview Checklist

Before writing code, make sure you can answer each of these

```text
Is a blocked cell blocked for this path only, or for the whole search forever?
Does the undo run on the failing exit path as well as the succeeding one?
Am I marking in the board with a sentinel, or in a separate visited set, and why?
Is the completion check before the bounds check, so a word ending on the border still matches?
Does the search stop at the first solution, or does it have to count all of them?
If it stops early, is the half-unwound state the deliverable or a bug?
For a placement board, what are the resources a choice consumes, and is every one of them released?
Do I need to restart the search from every cell, or is there a single fixed start?
What prunes a branch before it reaches the bottom: an overshot total, a used column, a mismatched character?
Are two branches symmetric copies of each other, so that trying one of them is enough?
Am I copying anything mutable before saving it into the output?
```
