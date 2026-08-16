# Geometry Basics

A **point** in the plane is an ordered pair of numbers `(x, y)`, where `x` says how
far right it sits and `y` says how far up. That is a different convention from the
`(row, column)` pairs used for [matrix coordinates](01_matrix_coordinates.md),
where the first number counts *downward*. Interview problems hand you points as
`[x, y]` lists, so the first coordinate is horizontal and the second is vertical,
and the plane is infinite in all four directions rather than clipped to a grid of
cells

Almost every geometry question in an interview is one of three questions wearing
a costume:

- **How far apart are these two points?** Closest pair, k nearest, "is this a
  square", "is this a valid triangle"
- **Which way does this corner turn?** Collinearity, triangle area, convex hull,
  "is this polygon convex", "do these segments cross"
- **Does this box fit against that box?** Rectangle overlap, covered area,
  "do these rectangles tile a bigger one"

The useful thing about all three is that the coordinates you are given are almost
always **integers**, and every one of these questions can be answered without ever
producing a non-integer. Squared distance instead of distance, a pair of integers
instead of a slope, and a cross product instead of an angle. Integers compare
exactly and hash exactly, so the answers come out right and the code has no
tolerance constant in it

> This topic covers squared and Manhattan distance, the reduced direction pair that
> replaces a slope, the cross product and the turn it measures, the convex hull
> built from it, and axis-aligned rectangles as pairs of intervals

## Why A Float Slope Is The Wrong Way To Describe A Line

Take *Max Points On A Line*: given a list of points, find the largest number of
them that lie on one straight line. Two points always define a line, so the natural
plan is to fix one point as an anchor, compute the slope from it to every other
point, and count how many share a slope. Same slope from the same anchor means
same line, so the biggest group wins

Slope is `rise over run`, so the code writes itself:

```text
slope from (x1, y1) to (x2, y2)  =  (y2 - y1) / (x2 - x1)
```

That plan dies on the first vertical line, and it dies loudly. Two points with the
same `x` give `x2 - x1 == 0`, and Python answers with a `ZeroDivisionError` reading
"division by zero" rather than a slope, because a vertical line genuinely has no
slope. It is not a precision problem, it is that the quantity does not exist

The reflex is to patch it. Store the string `"inf"` for vertical lines, and now you
need a second patch for duplicate points, where `x2 - x1` and `y2 - y1` are both
zero and the pair does not define a line at all. Then you notice the key is a float
and floats are only safe to compare when every intermediate value stayed exactly
representable, so you start worrying about a third case. Three special branches,
each remembered under time pressure, all caused by one division

The fix is to not divide. A line through the anchor is completely described by the
**direction** you travel to leave it, and direction is just the pair `(dx, dy)`. The
only problem with keeping the raw pair is that `(1, 2)`, `(2, 4)`, and `(-3, -6)`
all point along the same line but are three different pairs, so they would land in
three different buckets. Divide both by their greatest common divisor and fix the
sign, and every pair along one line collapses to a single canonical pair of
integers

> "I am not going to key on the slope, because a vertical line has no slope and the
> division raises. I will key on the direction `(dx, dy)` reduced by its gcd with the
> sign normalized, which is exact integer equality and needs no special case for
> verticals"

## The Reduced Direction Pair

Reducing by [gcd](03_gcd_lcm.md) is what makes `(2, 4)` and `(1, 2)` the same key,
because dividing both components by `2` leaves the ratio untouched while shrinking
the pair to its smallest integer form. That still leaves `(1, 2)` and `(-1, -2)`,
which point in opposite directions along the *same* line, so a sign rule is needed
too: force `dx` positive, and when `dx` is zero force `dy` positive

```python
from collections.abc import Sequence
from math import gcd

Point = Sequence[int]


def direction(a: Point, b: Point) -> tuple[int, int]:
    dx, dy = b[0] - a[0], b[1] - a[1]
    g = gcd(dx, dy)
    if g == 0:
        return (0, 0)
    dx, dy = dx // g, dy // g
    if dx < 0 or (dx == 0 and dy < 0):
        dx, dy = -dx, -dy
    return (dx, dy)


assert direction((0, 0), (2, 4)) == (1, 2)
assert direction((0, 0), (-2, -4)) == (1, 2)
assert direction((0, 0), (0, 7)) == (0, 1)
assert direction((0, 0), (0, -7)) == (0, 1)
assert direction((3, 3), (5, 3)) == (1, 0)
assert direction((3, 3), (3, 3)) == (0, 0)
```

**The four lines that carry the idea**:

- `gcd(dx, dy)` reduces the pair to lowest terms, and `math.gcd` uses absolute
  values internally, so it is safe on negative components. `g` divides both exactly
  by definition, which is why the `//` truncation never loses anything
- `if g == 0` is the duplicate-point case, since `gcd(0, 0) == 0` and dividing by it
  would raise. Returning `(0, 0)` gives duplicates their own bucket instead of
  crashing, and *Max Points On A Line* wants them counted rather than skipped
- `if dx < 0 or (dx == 0 and dy < 0)` flips the whole pair so that every line has
  exactly one representative. Without it a horizontal line seen leftward and the
  same line seen rightward hash to different keys and the count comes out halved
- Vertical lines need no branch at all. `dx` is `0`, `gcd(0, 7)` is `7`, and the key
  is `(0, 1)`, which is a perfectly ordinary tuple

Anchoring at each point in turn and grouping the rest by direction gives the whole
solution. Every line with `k` points on it gets seen from whichever of its points
comes first in the list, with the other `k - 1` in one bucket, so scanning all
anchors is guaranteed to catch it:

```python
from collections import defaultdict


def max_points(points: list[list[int]]) -> int:
    pts = [(x, y) for x, y in points]
    if len(pts) <= 2:
        return len(pts)
    best = 1
    for i, anchor in enumerate(pts):
        groups: dict[tuple[int, int], int] = defaultdict(int)
        for other in pts[i + 1 :]:
            groups[direction(anchor, other)] += 1
        best = max(best, 1 + max(groups.values(), default=0))
    return best


assert max_points([[1, 1], [2, 2], [3, 3]]) == 3
assert max_points([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4
assert max_points([[0, 0], [0, 1], [0, 2], [1, 1]]) == 3
assert max_points([[0, 0]]) == 1
```

The inner loop starts at `i + 1` rather than at `0`, because a pair looked at from
both ends counts the same line twice and costs double for nothing. The `1 +` adds
the anchor itself back, since the group counts only the *other* points. The
`default=0` handles the final anchor, which has nothing after it

## Distance Without The Square Root

The distance between two points comes from the Pythagorean theorem: the horizontal
gap and the vertical gap are the two legs of a right triangle, and the straight-line
distance is the hypotenuse, so `d = sqrt(dx² + dy²)`. That straight-line measure is
called the **Euclidean distance**

The square root is almost always wasted work. Squaring is an increasing function on
non-negative numbers, so for any two non-negative distances `d1 < d2` holds exactly
when `d1² < d2²`, which means comparing squared distances gives the same ordering
and the same equalities as comparing real ones. Anything decided by "which is
closer", "are these two the same length", or "sort by distance" can be decided
entirely on `dx² + dy²`, and that quantity is an integer whenever the coordinates
are

Taking the root also costs you exactness. `math.sqrt(2) * math.sqrt(2)` evaluates to
`2.0000000000000004`, not `2`, because the true root is irrational and the float
holds a rounded copy of it. Once a value has been through `sqrt` you are comparing
approximations, and equality tests on approximations are the ones that silently
return the wrong answer

The other metric worth knowing is **Manhattan distance**, also called taxicab
distance, which is `|dx| + |dy|`. It measures how far you would travel if you could
only move horizontally and vertically, like a taxi on a city grid that cannot cut
through buildings. It is the natural distance whenever movement is axis-aligned, and
unlike the Euclidean distance it is already an integer with no root involved

```text
                            (4, 3)
                              *
                        .  .  |
                  .  .        |     Euclidean: sqrt(4² + 3²) = 5,
            .  .              |       the straight diagonal cut
      .  .                    |
   *--------------------------+     Manhattan: |4 - 0| + |3 - 0| = 7,
 (0, 0)                    (4, 0)     four steps right, then three up
```

Every staircase path from `(0, 0)` to `(4, 3)` that only goes right and up has the
same Manhattan length of `7`, because it must make exactly four rightward moves and
three upward moves in some order. That is why the metric ignores the route entirely
and only looks at the two gaps

```python
def dist2(a: Point, b: Point) -> int:
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def manhattan(a: Point, b: Point) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


assert dist2((0, 0), (3, 4)) == 25
assert manhattan((0, 0), (3, 4)) == 7
assert dist2((-1, -1), (2, 3)) == 25
assert manhattan((-1, -1), (2, 3)) == 7
assert dist2((2, 2), (2, 2)) == 0 and manhattan((2, 2), (2, 2)) == 0
```

Squared distance is exactly what *Valid Square* needs. Four points form a square
when, of the six distances between all pairs, four are equal sides and two are equal
diagonals, and the diagonal squared is twice the side squared by Pythagoras applied
to two perpendicular sides of equal length. Sorting the six squared distances puts
the four sides first and the two diagonals last, with no need to know which point is
adjacent to which:

```python
def valid_square(p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
    pts = [p1, p2, p3, p4]
    sides = sorted(dist2(pts[i], pts[j]) for i in range(4) for j in range(i + 1, 4))
    return sides[0] > 0 and sides[0] == sides[3] and sides[4] == sides[5] and sides[4] == 2 * sides[0]


assert valid_square([0, 0], [1, 1], [1, 0], [0, 1]) is True
assert valid_square([1, 0], [-1, 0], [0, 1], [0, -1]) is True
assert valid_square([0, 0], [1, 1], [1, 0], [0, 12]) is False
assert valid_square([0, 0], [0, 0], [0, 0], [0, 0]) is False
```

`sides[0] > 0` is the degenerate guard, and it is the check people forget. Four
copies of the same point produce six distances of zero, which satisfies every
equality in the return statement, so without that first clause a single point
reports itself as a square

The same squared-distance key is all *K Closest Points to Origin* needs on top of
the [capped heap from top-k](../../08_heaps/notes/02_top_k.md). Sort or heap on
`x² + y²` and never call `sqrt`, because the ranking is identical and the keys stay
integers

## Which Way The Corner Turns

Distance says how far apart two points are but says nothing about arrangement.
Three points can be the same three distances apart and still be laid out as a left
turn or a right turn, and telling those apart is what the **cross product** does

For three points `o`, `a`, and `b`, treat `a - o` and `b - o` as two arrows leaving
`o`, and compute:

```text
cross(o, a, b) = (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)
```

The sign of that single number answers the arrangement question:

```text
   cross > 0                 cross < 0                cross = 0
   counterclockwise          clockwise                collinear

        b                         a                        b
       /                         /                        /
      /                         /                        a
     o------a                  o------b                  /
                                                        o
   turning left at a         turning right at a      no turn, all on one line
```

The magnitude says something too. `|cross(o, a, b)|` is the area of the
parallelogram spanned by the two arrows, so half of it is the area of the triangle
`o a b`. That is the **shoelace formula** for a triangle, and it is why the same
expression answers both "which way does this turn" and "how big is this triangle"

```python
def cross(o: Point, a: Point, b: Point) -> int:
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


assert cross((0, 0), (1, 0), (1, 1)) == 1
assert cross((0, 0), (1, 0), (1, -1)) == -1
assert cross((0, 0), (1, 1), (3, 3)) == 0
assert cross((0, 0), (4, 0), (0, 3)) == 12
assert cross((0, 0), (0, 0), (5, 5)) == 0
```

`cross(o, a, b) == 0` is the collinearity test, and it is worth noticing that it is
the *same* fact the reduced direction pair encodes. Both say `dy1 * dx2 == dy2 * dx1`
after multiplying out, which is the cross-multiplied form of "the two slopes are
equal" with the division removed. Use the direction pair when you need to *group*
many points by line, since a tuple can be a dictionary key, and use the cross product
when you only need to *test* one triple

*Largest Triangle Area* is then a direct application, since with at most 50 points
the interviewer expects all triples to be enumerated:

```python
def largest_triangle_area(points: list[list[int]]) -> float:
    n = len(points)
    best = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                best = max(best, abs(cross(points[i], points[j], points[k])))
    return best / 2


assert largest_triangle_area([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]) == 2.0
assert largest_triangle_area([[1, 0], [0, 0], [0, 1]]) == 0.5
assert largest_triangle_area([[0, 0], [1, 1], [2, 2]]) == 0.0
```

The `abs` goes on the cross product and the halving happens once at the very end, so
every comparison inside the loop is between integers and only the returned value is a
float. Three collinear points give area `0.0` rather than an error, which is the
right answer and the degenerate case to state out loud

## Wrapping A Rubber Band Around The Points

The **convex hull** of a set of points is the smallest convex shape containing all of
them, and the physical picture is exact: hammer a nail into every point, stretch a
rubber band around the outside, and let go. The band settles onto a subset of the
points, and those are the hull. *Erect the Fence* asks for exactly that, phrased as
the trees a fence must touch

Convex means the boundary never turns back on itself, so walking the hull
counterclockwise turns left at every vertex and never right. That is a cross-product
test, which is why the hull belongs in the same topic as the turn

**Andrew's monotone chain** builds it in two passes. Sort the points by `x`, then
sweep left to right building the **lower hull**, and sweep right to left building the
**upper hull**. During a sweep, keep a stack of the hull so far, and before pushing a
new point, pop the top while the last two stack entries plus the new point make a
non-left turn, because a point that is not a left turn is either inside the hull or
lying flat on an edge, and either way the rubber band does not touch it

```python
def convex_hull(points: list[tuple[int, int]]) -> list[tuple[int, int]]:
    pts = sorted(set(points))
    if len(pts) <= 2:
        return pts
    lower: list[tuple[int, int]] = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper: list[tuple[int, int]] = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


assert convex_hull([(0, 0), (1, 0), (2, 0), (2, 2), (0, 2), (1, 1)]) == [
    (0, 0),
    (2, 0),
    (2, 2),
    (0, 2),
]
assert convex_hull([(0, 0), (1, 1), (2, 2)]) == [(0, 0), (2, 2)]
assert convex_hull([(0, 0), (1, 1)]) == [(0, 0), (1, 1)]
assert convex_hull([(0, 0), (0, 0)]) == [(0, 0)]
```

**The parts that are easy to get wrong**:

- `sorted(set(points))` sorts by `x` and breaks ties by `y`, because tuples compare
  lexicographically. The `set` removes duplicate points, which a repeated point needs
  because `cross` reads two copies of the same point as a zero turn: the `<= 0`
  condition then pops one copy back off, so most duplicates are harmless, but an input
  that is nothing *but* copies of one point pops down to a single entry and then
  re-pushes, so each chain ends holding two copies and the point comes back listed
  twice instead of once
- Two passes are needed because sorting by `x` gives no information about whether a
  point belongs above or below the shape. The lower pass finds the bottom boundary,
  the reversed pass finds the top, and together they close the loop
- `lower[:-1] + upper[:-1]` drops the last element of each chain, since the leftmost
  and rightmost points appear as an endpoint of both chains and would otherwise be
  listed twice
- The `<= 0` pop condition discards collinear points, giving a hull with only true
  corners. *Erect the Fence* wants every point the fence physically touches, including
  ones lying flat along an edge, so it uses `< 0` instead and then deduplicates,
  because with the weaker condition a point can be appended by both passes

### Dry Run: Six Points, Two Rejections

Six points where `(1, 1)` sits in the middle of the square and `(1, 0)` sits exactly
on the bottom edge between `(0, 0)` and `(2, 0)`. After `sorted(set(...))` the order
is `(0,0), (0,2), (1,0), (1,1), (2,0), (2,2)`

```text
lower hull, sweeping left to right

push (0,0)                                        lower=[(0,0)]
push (0,2)                                        lower=[(0,0),(0,2)]
see (1,0)  cross((0,0),(0,2),(1,0)) = -2 <= 0     POP (0,2), right turn
push (1,0)                                        lower=[(0,0),(1,0)]
push (1,1)                                        lower=[(0,0),(1,0),(1,1)]
see (2,0)  cross((1,0),(1,1),(2,0)) = -1 <= 0     POP (1,1), interior point
see (2,0)  cross((0,0),(1,0),(2,0)) =  0 <= 0     POP (1,0), collinear on the edge
push (2,0)                                        lower=[(0,0),(2,0)]
push (2,2)                                        lower=[(0,0),(2,0),(2,2)]
```

The two pops on the `(2, 0)` step are the whole mechanism. `(1, 1)` came off because
`cross` was `-1`, a right turn, meaning the chain had bulged inward and `(1, 1)` sits
strictly inside the shape. `(1, 0)` then came off because `cross` was exactly `0`,
meaning it lies flat on the straight run from `(0, 0)` to `(2, 0)` and adds no corner.
That second pop is the line *Erect the Fence* has to weaken, because a tree standing
on the fence line still has the fence touching it

Note that `(0, 2)` was pushed and then popped as well. Being early in sorted order
buys a point nothing, since the lower hull only keeps what stays on the bottom
boundary, and `(0, 2)` is a top point that the reversed pass picks up instead

```text
upper hull, sweeping right to left, ends as [(2,2),(0,2),(0,0)]
answer = lower[:-1] + upper[:-1] = [(0,0),(2,0)] + [(2,2),(0,2)]
       = [(0,0),(2,0),(2,2),(0,2)]
```

The four corners of the square come out counterclockwise, and both the interior point
and the edge point are gone

## Rectangles Are Two Intervals Wearing A Costume

An **axis-aligned rectangle** is given as `[x1, y1, x2, y2]`, the bottom-left and
top-right corners, and its sides run parallel to the axes. That shape is completely
described by two [intervals](../../13_intervals/notes/01_interval_basics.md): the
interval `[x1, x2]` on the horizontal axis and `[y1, y2]` on the vertical one

Two such rectangles overlap exactly when *both* pairs of intervals overlap, because a
shared point needs a shared `x` and a shared `y` at the same time. The one-dimensional
overlap test is settled already, so the two-dimensional version is that test twice
joined by `and`. *Rectangle Overlap* asks for overlap of positive area, which makes
each comparison strict, since rectangles that merely touch along an edge share a line
of zero width:

```python
def is_rectangle_overlap(rec1: list[int], rec2: list[int]) -> bool:
    return rec1[0] < rec2[2] and rec2[0] < rec1[2] and rec1[1] < rec2[3] and rec2[1] < rec1[3]


def compute_area(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
    wide = max(0, min(ax2, bx2) - max(ax1, bx1))
    tall = max(0, min(ay2, by2) - max(ay1, by1))
    return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - wide * tall


assert is_rectangle_overlap([0, 0, 2, 2], [1, 1, 3, 3]) is True
assert is_rectangle_overlap([0, 0, 1, 1], [1, 0, 2, 1]) is False
assert is_rectangle_overlap([0, 0, 1, 1], [2, 2, 3, 3]) is False
assert compute_area(-3, 0, 3, 4, 0, -1, 9, 2) == 45
assert compute_area(-2, -2, 2, 2, -2, -2, 2, 2) == 16
assert compute_area(0, 0, 0, 0, -1, -1, 1, 1) == 4
```

`compute_area` is inclusion-exclusion in two dimensions: add both areas, then
subtract the part counted twice. The intersection is itself a rectangle whose
horizontal span runs from the larger of the two lefts to the smaller of the two
rights, which is why `max` and `min` appear crossed over. The `max(0, ...)` is the
disjoint case, because when the rectangles miss each other that subtraction goes
negative and would otherwise *add* phantom area. The zero-area rectangle in the last
assertion is the degenerate input worth checking

*Perfect Rectangle* asks whether a pile of rectangles tiles one big rectangle exactly,
with no gap and no double covering, and it takes two checks that are useless
separately. The areas must sum to the area of the bounding box, which rules out gaps
and overlaps in total but not one gap paid for by one overlap elsewhere. The corners
must then cancel: every corner point in the interior of a perfect tiling is touched
by an even number of rectangles, so toggling each corner in and out of a set leaves
only the four corners of the bounding box behind

```python
def is_rectangle_cover(rectangles: list[list[int]]) -> bool:
    area = 0
    corners: set[tuple[int, int]] = set()
    x1 = y1 = float("inf")
    x2 = y2 = float("-inf")
    for a, b, c, d in rectangles:
        area += (c - a) * (d - b)
        x1, y1 = min(x1, a), min(y1, b)
        x2, y2 = max(x2, c), max(y2, d)
        for corner in ((a, b), (a, d), (c, b), (c, d)):
            corners ^= {corner}
    if area != (x2 - x1) * (y2 - y1):
        return False
    return corners == {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}


assert is_rectangle_cover([[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]) is True
assert is_rectangle_cover([[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]]) is False
assert is_rectangle_cover([[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [2, 2, 4, 4]]) is False
assert is_rectangle_cover([[0, 0, 1, 1]]) is True
```

`corners ^= {corner}` is symmetric difference with a one-element set, which adds the
point if absent and removes it if present, so the set ends up holding exactly the
points seen an odd number of times

Three more problems in this section belong to patterns established elsewhere and need
no new geometry. *The Skyline Problem* and *Rectangle Area II* are both
[sweep line](../../13_intervals/notes/04_sweep_line.md) problems, where the geometry
is only the observation that a building or rectangle is an interval that turns on at
one `x` and off at another. *Basic Calculator* is not geometry at all despite living
in this file, and is solved with the running sign and the
[stack](../../03_stacks_and_queues/notes/01_stack.md) that expression evaluation
always uses. *Self Crossing* is casework rather than a technique: a path that turns
the same way every time is a spiral, which either keeps shrinking and never touches
itself, or stops shrinking, and when it stops the crossing must involve one of the
previous three to five segments, so those are the only comparisons to write

## Worked Example: [Minimum Area Rectangle](https://leetcode.com/problems/minimum-area-rectangle/)

Given a set of points in the plane, find the smallest possible area of a rectangle
whose four corners are all in the set and whose sides are parallel to the axes. If no
such rectangle exists, the answer is zero

**Input**: `points`, a `list[list[int]]` where each entry is a pair `[x, y]`. All
points are distinct

**Output**: an `int`, the area of the smallest axis-aligned rectangle whose four
corners all appear in `points`, and `0` when no four points form such a rectangle.
The value is an exact integer area, not a count of rectangles and not a bounding box

The phrase that identifies the technique is **"sides parallel to the axes"**, because
it removes rotation from the problem entirely and forces the four corners into a rigid
pattern. The naive reading is to try every group of four points and check whether it
forms a rectangle, which is `O(n⁴)` and unusable at the input sizes these problems
carry

The saving observation is that an axis-aligned rectangle is fully determined by either
of its two diagonals. Pick any two points that share neither an `x` nor a `y`, treat
them as opposite corners, and the other two corners are forced to be `(x1, y2)` and
`(x2, y1)`. There is nothing to search, only a membership question, and that is a set
lookup

> "Because the sides are axis-parallel, any two points with different `x` and
> different `y` already pin down a rectangle. I only have to ask whether the other two
> corners exist, so I will hash every point into a set and check pairs in `O(1)`"

That turns `O(n⁴)` into `O(n²)`, one constant-time check per pair

Therefore,

1. Build a `set` of the points as tuples, because tuples are hashable while the input
   lists are not, and the whole speedup depends on corner lookup being `O(1)`
2. Sort the deduplicated points into a list so the pair loop can iterate each unordered
   pair exactly once, which is what pairing index `i` against everything before it does
3. For each pair, reject immediately when the two points share an `x` or share a `y`,
   because two such points lie on a common side rather than on a diagonal and pin down
   no rectangle
4. For a surviving pair `(x1, y1)` and `(x2, y2)`, ask whether both `(x1, y2)` and
   `(x2, y1)` are in the set. Those are the only two points that could complete this
   rectangle, so a single failed lookup rejects the pair outright
5. When both are present, the area is `|x1 - x2| * |y1 - y2|`, the width times the
   height, and it needs the absolute values because the pair order says nothing about
   which corner is left or lower
6. Keep the running minimum, seeded at `0` to double as the "nothing found" answer,
   which means the update has to test `best == 0` first rather than calling `min`
   blindly
7. Return the running minimum, which is already `0` in the case where no pair ever
   completed a rectangle

```python
def min_area_rect(points: list[list[int]]) -> int:
    seen = {(x, y) for x, y in points}
    pts = sorted(seen)
    best = 0
    for i, (x1, y1) in enumerate(pts):
        for x2, y2 in pts[:i]:
            if x1 == x2 or y1 == y2:
                continue
            if (x1, y2) in seen and (x2, y1) in seen:
                area = abs(x1 - x2) * abs(y1 - y2)
                if best == 0 or area < best:
                    best = area
    return best


assert min_area_rect([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]) == 4
assert min_area_rect([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2], [4, 1], [4, 3]]) == 2
assert min_area_rect([[1, 1], [2, 2]]) == 0
assert min_area_rect([]) == 0
```

The five-point example traces as follows, with the sorted list
`(1,1), (1,3), (2,2), (3,1), (3,3)`:

```text
(1,3) & (1,1)   share x = 1                                       skip, not a diagonal
(2,2) & (1,1)   needs (2,1) and (1,2)   both missing              REJECT
(2,2) & (1,3)   needs (2,3) and (1,2)   both missing              REJECT
(3,1) & (1,1)   share y = 1                                       skip, not a diagonal
(3,1) & (1,3)   needs (3,3) and (1,1)   both present  area = 4    take, best = 4
(3,1) & (2,2)   needs (3,2) and (2,1)   both missing              REJECT
(3,3) & (1,1)   needs (3,1) and (1,3)   both present  area = 4    not smaller, keep 4
(3,3) & (1,3)   share y = 3                                       skip, not a diagonal
(3,3) & (2,2)   needs (3,2) and (2,3)   both missing              REJECT
(3,3) & (3,1)   share x = 3                                       skip, not a diagonal
```

The centre point `(2, 2)` is rejected against every partner it is paired with, which
is the useful thing to watch. It is inside the square and shares no corner structure
with anything, so all four pairings that involve it die on a missing corner rather
than on a coordinate clash. The rectangle itself is found twice, once from each of its
two diagonals, and the second sighting is correctly kept out by the `area < best` test
rather than by any extra bookkeeping

- **Time Complexity:** `O(n²)`, because the double loop examines each of the roughly
  `n² / 2` unordered pairs once and does two `O(1)` average-case set lookups per pair,
  and the `sorted` call adds only `O(n log n)`
- **Space Complexity:** `O(n)`, because the point set and the sorted list each hold one
  entry per distinct input point and nothing per pair is stored

## Time and Space Complexity

**Primitives**, where `a` and `b` are single points

| Operation               | Time                                                                                                                                                                            | Space                                                                                                                      |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `dist2` and `manhattan` | `O(1)`: two subtractions and two multiplications or absolute values, with no loop and no root                                                                                   | `O(1)`: the result is one integer and nothing is allocated                                                                 |
| `direction`             | `O(log m)`: where `m` is the smaller of the two coordinate gaps in absolute value, since Euclid's algorithm inside `gcd` dominates the constant-time subtractions and sign flip | `O(1)`: it returns a two-element tuple and holds no intermediate structure                                                 |
| `cross`                 | `O(1)`: four subtractions, two multiplications, one subtraction, all on integers                                                                                                | `O(1)`: one integer, and Python big integers only grow past machine words for coordinates far beyond interview constraints |

**Problems in this section**, where `n` is the number of points or rectangles

| Approach                                               | Time                                                                                                                                       | Space                                                                                                         |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| *Max Points On A Line* by reduced direction            | `O(n² log C)`: `n` anchors times `n` other points, each costing one `gcd` of coordinates bounded by `C`                                    | `O(n)`: one `defaultdict` per anchor holding at most `n - 1` direction keys, discarded before the next anchor |
| *Max Points On A Line* by testing every triple         | `O(n³)`: three nested loops with one `cross` inside, which is the version to name and reject out loud                                      | `O(1)`: no grouping structure, which is the only thing it has going for it                                    |
| *Minimum Area Rectangle* by diagonal pairs             | `O(n²)`: every unordered pair checked once with two `O(1)` average set lookups                                                             | `O(n)`: the point set, which is what buys the constant-time corner lookup                                     |
| *Minimum Area Rectangle* by every group of four points | `O(n⁴)`: enumerating quadruples before checking any of them, and unusable at real input sizes                                              | `O(1)`: it stores nothing, and stores nothing usefully                                                        |
| *Valid Square*                                         | `O(1)`: exactly six pairwise distances and a six-element sort on a fixed input of four points                                              | `O(1)`: the six-element list has fixed length regardless of anything                                          |
| *Largest Triangle Area*                                | `O(n³)`: every triple of points with one `cross` each, which the small input bound makes acceptable                                        | `O(1)`: one running maximum integer                                                                           |
| Convex hull by monotone chain                          | `O(n log n)`: the sort dominates, since each of the two sweeps pushes every point once and pops it at most once, giving `O(n)` across both | `O(n)`: the sorted list plus the two chains, which together hold at most every point                          |
| *Rectangle Overlap* and *Rectangle Area*               | `O(1)`: four comparisons, or a fixed handful of `min`/`max` calls and three multiplications                                                | `O(1)`: only the clamped width and height                                                                     |
| *Perfect Rectangle*                                    | `O(n)`: one pass adding four corners and one area per rectangle, with average-case `O(1)` set toggles                                      | `O(n)`: the corner set, which holds up to `4n` points before the cancellations reduce it                      |

The convex hull's inner `while` looks like it could make one push `O(n)`, and it can,
but each point is pushed exactly once per sweep and can therefore be popped at most
once per sweep, so the total pop work across the whole sweep is `O(n)`. That is the
same amortization argument the
[monotonic stack](../../03_stacks_and_queues/notes/03_monotonic_stack.md) uses, and it
is worth saying out loud, because an interviewer who sees a loop inside a loop will
ask

## Summary

- A **point** is a pair `(x, y)` where the first coordinate is horizontal and the
  second is vertical, which is the opposite convention to the `(row, column)` pairs
  used for matrices. Interview inputs give points as `[x, y]` lists with integer
  coordinates, and that integrality is the property worth protecting
  - Every core geometry question — how far apart, which way does it turn, does this box
    fit — can be answered without producing a single non-integer
- **Squared Euclidean distance** is `dx² + dy²`, and it should be used instead of the
  real distance whenever the problem only compares, sorts, or tests equality of
  distances. Squaring is increasing on non-negative numbers, so `d1 < d2` holds exactly
  when `d1² < d2²`, which means the ordering is identical
  - `math.sqrt` is both unnecessary work and lossy, since `math.sqrt(2) * math.sqrt(2)`
    evaluates to `2.0000000000000004` rather than `2`
- **Manhattan distance** is `|dx| + |dy|`, the distance travelled when only horizontal
  and vertical moves are allowed, like a taxi on a city grid. It is already an integer,
  and it is the right metric whenever movement is axis-aligned rather than free
- A line through an anchor point is described by the **reduced direction pair**, which
  is `(dx, dy)` divided by `gcd(dx, dy)` with the sign normalized so `dx` is positive,
  or `dy` is positive when `dx` is zero
  - Never use `dy / dx` as a slope key, because a vertical line raises
    `ZeroDivisionError` rather than producing a slope, and patching that costs a special
    case for verticals and another for duplicate points
  - Duplicate points give `gcd(0, 0) == 0`, so guard the division and give them their
    own `(0, 0)` bucket rather than crashing
- The **cross product** `(a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)` measures
  the turn from `o → a` to `o → b`. Positive means a counterclockwise left turn,
  negative means clockwise, and exactly zero means the three points are collinear
  - Its absolute value is twice the area of triangle `o a b`, which is the **shoelace
    formula** and what *Largest Triangle Area* uses directly
  - Collinearity by `cross == 0` and equality of reduced direction pairs are the same
    statement, so use the pair when grouping many points and the cross product when
    testing one triple
- The **convex hull** is the smallest convex shape containing every point, the rubber
  band stretched around a board of nails. **Andrew's monotone chain** sorts by `x`, then
  builds a lower chain left to right and an upper chain right to left, popping the stack
  top whenever the last two entries and the new point fail to turn left
  - The cost is `O(n log n)` because the sort dominates, since each sweep pushes every
    point once and pops it at most once, making both sweeps `O(n)` in total
  - `cross <= 0` pops collinear points and gives only true corners, while *Erect the
    Fence* needs `< 0` plus deduplication so that points lying flat on an edge survive
- An **axis-aligned rectangle** `[x1, y1, x2, y2]` is two intervals, one per axis, so
  two rectangles overlap exactly when both pairs of intervals overlap. Overlap area is
  `max(0, min of rights - max of lefts)` times the same expression vertically, and the
  `max(0, ...)` is what stops a disjoint pair adding phantom area
  - *Rectangle Area* is then inclusion-exclusion: both areas added, the intersection
    subtracted once
  - *Perfect Rectangle* pairs a total-area check against the bounding box with a corner
    parity check, since neither catches a gap paid for by an overlap on its own
- The mistakes that cost the most are calling `sqrt` and then comparing floats for
  equality, dividing to get a slope and meeting a vertical line, and forgetting the
  degenerate guard where four identical points satisfy every equality test in a square
  check

## Interview Checklist

Before writing code, make sure you can answer each of these

```text
Am I only comparing distances, which means I can work in squared distance and never call sqrt?
Is the movement in this problem free (Euclidean) or axis-aligned (Manhattan)?
Do I need to group points by line, which wants a reduced direction pair as a hash key?
Have I handled the vertical line, where dx is 0 and a slope does not exist?
Have I handled duplicate points, where gcd(0, 0) is 0 and there is no direction at all?
Did I normalize the sign of the direction pair so one line has exactly one key?
Do I need the sign of the cross product (turn direction) or its magnitude (area)?
Is my degenerate input covered: all points identical, all collinear, fewer than three points?
Are these rectangles axis-aligned, so I can treat each one as two independent intervals?
Does the overlap test need strict comparisons, because touching edges have zero area?
For the convex hull, do I keep collinear boundary points or only true corners?
Can I justify the amortized O(n) in the hull's push-and-pop sweep out loud?
```
