# Monotonic Stacks

A **monotonic stack** is a [stack](01_stack.md) whose values stay ordered from
bottom to top. A decreasing stack never rises as you read upward, while an
increasing stack never falls.

The stack is not sorted afterward. It stays ordered because every arriving value
pops the entries that it makes useless before joining the top itself.

```text
values arriving:  2, 1, 2, 4

before 4 arrives, the decreasing stack holds indices 0 and 2

index     0   2
value     2   2     <- equal values are still waiting

4 pops index 2 -> 4 is its next greater value
4 pops index 0 -> 4 is its next greater value
4 is pushed    -> stack=[3]
```

The useful mental model is a list of **unresolved candidates**. An index stays on
the stack while it waits for a later value to answer it. When that answer arrives,
the index is resolved and popped immediately.

The comparison controls both the order and the treatment of equal values. For a
strictly greater answer, pop while `top < current`; an equal value is not greater,
so it stays. For a greater-or-equal answer, pop while `top <= current`. This
**equal-value policy** must be chosen from the problem statement rather than from
memory.

## When A Later Value Answers An Earlier One

Monotonic stacks usually appear when a problem asks for one of these:

- The nearest greater or smaller value in one direction, such as the next warmer
  day or the previous lower price
- The distance to that value, which means the stack should hold indices
- The widest span over which one value remains the minimum or maximum, as in a
  histogram rectangle
- Each value's contribution across many subarrays, where nearest boundaries tell
  how many subarrays choose that value
- An output that improves when a worse recent choice is removed, as in Remove K
  Digits or Remove Duplicate Letters

The common signal is that a value arriving now can settle one or more earlier
values. If an answer depends only on values already seen and never needs revision,
a running variable may be enough and the stack is unnecessary.

## Why Scanning Forward Repeats Work

The direct solution for a next-greater query starts at every index and scans
right until it finds a larger value.

```python
def next_greater_naive(nums: list[int]) -> list[int]:
    answer = [-1] * len(nums)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                answer[i] = nums[j]
                break
    return answer


assert next_greater_naive([5, 4, 3, 9]) == [9, 9, 9, -1]
assert next_greater_naive([2, 1, 2, 4, 3]) == [4, 2, 4, -1, -1]
assert next_greater_naive([3, 3, 3]) == [-1, -1, -1]
assert next_greater_naive([]) == []
```

On `[5, 4, 3, 9]`, each of 5, 4, and 3 separately walks toward the same 9. A
decreasing prefix followed by one large value makes this `O(n²)` because nearly
the same suffix is searched from every starting position.

Reverse who does the searching. Let 9 look backward once and settle every
smaller value still waiting. The unresolved values are already decreasing:
if an earlier pending value were smaller than a later pending value, the later
one would already have resolved it. Therefore, all values the newcomer can
resolve sit together at the top of a stack.

## Resolving Next-Greater Answers In One Pass

Store indices rather than bare values. An index can recover its value with one
lookup and also gives the position needed for a distance or width.

```python
def next_greater(nums: list[int]) -> list[int]:
    answer = [-1] * len(nums)
    stack: list[int] = []  # indices; values decrease bottom to top

    for i, value in enumerate(nums):
        while stack and nums[stack[-1]] < value:
            waiting = stack.pop()
            answer[waiting] = value
        stack.append(i)

    return answer


assert next_greater([2, 1, 2, 4, 3]) == [4, 2, 4, -1, -1]
assert next_greater([5, 4, 3, 9]) == [9, 9, 9, -1]
assert next_greater([3, 3, 3]) == [-1, -1, -1]
assert next_greater([]) == []
```

The answer starts with `-1` because any index left on the stack never finds a
greater value. The pop condition is a `while`, not an `if`, because one arriving
value may answer several waiting indices.

Trace `[2, 1, 2, 4, 3]`:

```text
i=0 value=2   push                       stack idx=[0]     values=[2]
i=1 value=1   2 is not smaller; push    stack idx=[0,1]   values=[2,1]
i=2 value=2   pop 1 -> answer[1]=2
                equal 2 does not pop     stack idx=[0,2]   values=[2,2]
i=3 value=4   pop 2 -> answer[2]=4
              pop 0 -> answer[0]=4       stack idx=[3]     values=[4]
i=4 value=3   4 is not smaller; push    stack idx=[3,4]   values=[4,3]
end           indices 3 and 4 unresolved; keep -1

answer = [4, 2, 4, -1, -1]
```

The equal values at `i = 2` are the rejected pop. Since the question asks for a
**strictly** greater value, index 0 must keep waiting. Using `<=` would incorrectly
claim that the equal 2 is its answer.

## Choosing Direction, Comparison, And Answer Time

Four common relationships share the same loop:

| Relationship              | Remove candidates while | Order left on stack | When the answer becomes known         |
| ------------------------- | ----------------------- | ------------------- | ------------------------------------- |
| Next strictly greater     | `top < current`         | Decreasing          | When the candidate pops               |
| Next strictly smaller     | `top > current`         | Increasing          | When the candidate pops               |
| Previous strictly greater | `top <= current`        | Strictly decreasing | From the surviving top before pushing |
| Previous strictly smaller | `top >= current`        | Strictly increasing | From the surviving top before pushing |

For “next,” the arriving value is the answer for every entry it pops. For
“previous,” remove entries that cannot qualify, then read the nearest survivor at
the top. If the wording allows equality, change the strictness deliberately.

This is where duplicate values become important in span and contribution
problems. If equal values may both claim the same subarray, it is counted twice.
A common policy is strict on one boundary and non-strict on the other, such as
previous strictly smaller plus next smaller-or-equal. The asymmetry assigns a run
of equal values to exactly one representative.

## Turning Boundaries Into Spans

Largest Rectangle In Histogram asks for the largest rectangle that fits beneath
a row of bar heights. If bar `j` supplies the rectangle's height, it can extend
until the first shorter bar on each side.

```text
heights   2   1   5   6   2   3
                  |---|

height 5 extends across indices 2..3
the shorter bars at indices 1 and 4 stop it
width=2, area=5*2=10
```

An increasing stack finds both boundaries when a bar pops. The arriving shorter
bar is the right boundary, and the new stack top after the pop is the left
boundary.

```python
def largest_rectangle_area(heights: list[int]) -> int:
    bars = heights + [0]
    stack: list[int] = []
    best = 0

    for right, height in enumerate(bars):
        while stack and bars[stack[-1]] >= height:
            bar_height = bars[stack.pop()]
            left = stack[-1] if stack else -1
            width = right - left - 1
            best = max(best, bar_height * width)
        stack.append(right)

    return best


assert largest_rectangle_area([2, 1, 5, 6, 2, 3]) == 10
assert largest_rectangle_area([2, 4]) == 4
assert largest_rectangle_area([1, 2, 3]) == 4
assert largest_rectangle_area([5]) == 5
assert largest_rectangle_area([]) == 0
```

The final zero is a **sentinel**, a fake shortest bar that forces every real bar
to pop. Without it, an increasing input such as `[1, 2, 3]` reaches the end with
all candidates unresolved and never measures them. Reading `left` after the pop
is essential, and `right - left - 1` counts only the bars between the two shorter
boundaries.

The same boundaries support contribution counting. If `left` is the chosen
previous-smaller boundary, `right` is the chosen next-smaller boundary, and `j`
is the current index, then `j - left` starting points and `right - j` ending
points make `nums[j]` the minimum:

```text
contribution = nums[j] * (j - left) * (right - j)
```

Sum Of Subarray Minimums needs one concrete duplicate policy. The implementation
below pops on `>=`, so the arriving index is the **next smaller-or-equal**
boundary. After those equal values pop, the surviving stack top is the **previous
strictly smaller** boundary. That strict/non-strict pairing assigns every
subarray containing equal minima to exactly one index.

```python
def sum_subarray_mins(arr: list[int]) -> int:
    mod = 1_000_000_007
    stack: list[int] = []
    total = 0

    for right, value in enumerate(arr + [0]):
        while stack and arr[stack[-1]] >= value:
            j = stack.pop()
            left = stack[-1] if stack else -1
            left_choices = j - left
            right_choices = right - j
            total = (total + arr[j] * left_choices * right_choices) % mod
        stack.append(right)

    return total


assert sum_subarray_mins([3, 1, 2, 4]) == 17
assert sum_subarray_mins([11, 81, 94, 43, 3]) == 444
assert sum_subarray_mins([11, 11]) == 33
assert sum_subarray_mins([7]) == 7
```

The final zero is a sentinel because the problem's values are positive. For
`[11, 11]`, the first 11 owns the one-element subarray ending at index 0, while
the second owns its own one-element subarray and the two-element subarray. The
contributions are 11 and 22, not two copies of the same spans, so the total is 33.

Sum Of Subarray Ranges runs the contribution idea once for maxima and once for
minima, then subtracts. Maximal Rectangle builds a histogram from every matrix
row and reuses the rectangle routine.

## Variants In The Problem Set

The stack invariant stays useful even when the story changes:

**Remove K Digits** uses the stack as the smallest prefix built so far. While an
incoming digit is smaller than the top and deletions remain, removing that earlier
larger digit improves the number at the earliest possible position. If the scan
ends with deletions left, the number is already nondecreasing, so the least
damaging choice is to remove digits from the end. Finally, strip leading zeroes
and return `"0"` if nothing remains.

```python
def remove_k_digits(num: str, k: int) -> str:
    stack: list[str] = []

    for digit in num:
        while k and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    if k:
        del stack[-k:]

    answer = "".join(stack).lstrip("0")
    return answer or "0"


assert remove_k_digits("1432219", 3) == "1219"
assert remove_k_digits("10200", 1) == "200"
assert remove_k_digits("12345", 2) == "123"
assert remove_k_digits("10", 2) == "0"
```

On `"1432219"` with `k = 3`, the arrivals 3, 2, and the second 2 discard the
larger digits immediately before them, leaving `"1219"`. On `"12345"`, no
arrival can improve the prefix, so the remaining deletions come from the end.

**Remove Duplicate Letters** adds two pieces of state. `seen` prevents a letter
already in the answer from being pushed twice, while `remaining` says whether a
larger top letter is safe to pop because another copy still appears later.

```python
from collections import Counter


def remove_duplicate_letters(s: str) -> str:
    remaining = Counter(s)
    seen: set[str] = set()
    stack: list[str] = []

    for ch in s:
        remaining[ch] -= 1
        if ch in seen:
            continue
        while stack and stack[-1] > ch and remaining[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(ch)
        seen.add(ch)

    return "".join(stack)


assert remove_duplicate_letters("bcabc") == "abc"
assert remove_duplicate_letters("cbacdcbc") == "acdb"
assert remove_duplicate_letters("a") == "a"
assert remove_duplicate_letters("") == ""
```

For `"bcabc"`, the arriving `a` can pop both `c` and `b` because each still has a
copy remaining. For `"cbacdcbc"`, `d` cannot be popped after its last occurrence
has been used, even when a smaller character arrives.

**Trapping Rain Water** treats a popped bar as the bottom of a valley. If the pop
empties the stack, there is no left wall and therefore no trapped water. Otherwise
the new top is the left wall, the current index is the right wall, the usable
height is `min(left_height, right_height) - bottom_height`, and the width is
`right - left - 1`.

```python
def trap(heights: list[int]) -> int:
    stack: list[int] = []
    water = 0

    for right, right_height in enumerate(heights):
        while stack and heights[stack[-1]] < right_height:
            bottom = stack.pop()
            if not stack:
                break
            left = stack[-1]
            width = right - left - 1
            bounded_height = min(heights[left], right_height) - heights[bottom]
            water += width * bounded_height
        stack.append(right)

    return water


assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
assert trap([4, 2, 0, 3, 2, 5]) == 9
assert trap([0, 1, 0, 2]) == 1
assert trap([3, 2, 1]) == 0
assert trap([]) == 0
```

On `[0, 1, 0, 2]`, index 2 pops when the height-2 right wall arrives. Index 1 is
the left wall, so the width is `3 - 1 - 1 = 1`, the bounded height is
`min(1, 2) - 0 = 1`, and that layer contributes one unit of water.

- **Next Greater Element I** records next-greater answers in a map for a subset
  of queried values. **Next Greater Element II** scans `2 * n` positions with
  `i % n` to simulate a circular array, but pushes each real index only once
- **Online Stock Span** stores `(price, span)` and absorbs the spans of smaller or
  equal prices, so each `next()` call returns how far the current price dominates
  to the left
- **Asteroid Collision** is a related stack simulation rather than an ordered
  monotonic stack. An incoming left-moving asteroid repeatedly collides with the
  newest surviving right-moving asteroid
- **Car Fleet** sorts cars by position and stacks arrival times. A car with an
  earlier arrival time catches the fleet ahead and merges instead of forming a
  new fleet
- **132 Pattern** scans from right to left, using a decreasing stack of possible
  “3” values and a remembered popped value as the best “2” found so far

These are not separate templates to memorize. For each one, say what an entry
represents, what makes it obsolete, and what becomes known when it pops.

## Worked Example: [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

Given temperatures in chronological order, return how many days each day must
wait for a **strictly warmer** temperature. Return `0` when no warmer day follows.

**Input**: `temperatures`, a `list[int]` of daily temperatures in chronological
order, where `1 <= len(temperatures) <= 10^5` and each value is between 30 and 100

**Output**: a `list[int]` of the same length, where position `i` holds the number
of days you must wait after day `i` before a strictly warmer day arrives, and `0`
when no later day is warmer

Scanning forward from every day is correct but quadratic on a decreasing input,
because each day searches the entire remaining forecast and finds nothing. A
monotonic stack keeps only the indices still waiting. Their temperatures decrease
from bottom to top, and a warmer day resolves all colder days at the top.

> “I’ll store indices because the answer is a distance. When day `i` is warmer
> than the day at index `j` on top, `i` is the first warmer day for `j`, so I pop
> `j` and write `i - j`. Equal temperatures stay because the problem says
> strictly warmer.”

Therefore,

1. Fill `answer` with `0`, one slot per day, because that default is already the
   correct output for any day that never finds a warmer one, which removes the
   need for a cleanup pass at the end
2. Start an empty stack that holds **indices** rather than temperatures, since the
   answer is a distance and only an index can produce `i - waiting`
3. Walk the days from left to right, treating the current day `i` as the newcomer
   that may settle the unresolved days already on the stack
4. While the stack is non-empty and the temperature at the top index is **strictly
   less** than today's, pop that index, because today is the first warmer day it
   has seen, and record `i - waiting` as its wait. This is a `while` rather than an
   `if` because a single warm day can settle several colder days stacked above one
   another
5. Stop popping as soon as the top temperature is greater than or equal to today's.
   The equal case is the edge case worth naming out loud: an equal temperature is
   not strictly warmer, so that index stays and keeps waiting for a real increase
6. Push `i` onto the stack, since today is itself unresolved. Everything left below
   it is at least as warm, so the stack stays decreasing from bottom to top
7. When the scan ends, any index still on the stack never met a warmer day, and its
   slot already holds the `0` from step 1, so return `answer` as it stands

```python
def daily_temperatures(temperatures: list[int]) -> list[int]:
    answer = [0] * len(temperatures)
    stack: list[int] = []

    for i, temperature in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temperature:
            waiting = stack.pop()
            answer[waiting] = i - waiting
        stack.append(i)

    return answer


assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
assert daily_temperatures([30, 60, 90]) == [1, 1, 0]
assert daily_temperatures([75, 74, 73]) == [0, 0, 0]
```

- **Time Complexity:** `O(n)`, because each of the `n` indices is pushed once
  and popped at most once across the entire scan
- **Space Complexity:** `O(n)` auxiliary space, because a decreasing forecast
  never pops and leaves every index on the stack; the `O(n)` answer is output

Trace `[73, 74, 74, 71, 76]`:

```text
i=0 t=73   push                         stack=[0]
i=1 t=74   pop 0 -> wait 1              stack=[1]
i=2 t=74   equal is not warmer; push    stack=[1,2]    REJECTED POP
i=3 t=71   colder; push                 stack=[1,2,3]
i=4 t=76   pop 3 -> wait 1
             pop 2 -> wait 2
             pop 1 -> wait 3            stack=[4]
end         index 4 keeps default 0

answer = [1, 3, 2, 1, 0]
```

A fully decreasing input such as `[75, 74, 73]` performs no pops and returns
`[0, 0, 0]`. That is both the correctness edge case and the `O(n)` auxiliary
space case.

## Time and Space Complexity

Let `n` be the number of input values.

| Approach                      | Time                                                                                                      | Space                                                                              |
| ----------------------------- | --------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Monotonic stack               | `O(n)`: each index is pushed once and popped at most once, so all inner-loop iterations total at most `n` | `O(n)`: a monotonic input can leave every index waiting at once                    |
| Scan forward from every index | `O(n²)`: many indices repeatedly inspect the same suffix                                                  | `O(1)` auxiliary space: it needs no candidate structure beyond the required answer |

The nested `while` loop does not make the stack solution quadratic. One iteration
may pop many indices only because earlier iterations pushed those indices and did
not pop them. This one-push, one-pop count is an amortized `O(1)` amount of stack
work per input value and `O(n)` total.

## Summary

- A **monotonic stack** holds unresolved candidates in increasing or decreasing
  order, and an arriving value pops every candidate it makes obsolete
- Reach for it when a later value answers an earlier one, especially for nearest
  greater/smaller relationships, distances, span boundaries, and contributions
- Store indices when the answer needs a distance or width, because an index also
  recovers its value while a bare value cannot recover its position
- The comparison defines the meaning of equality: use `<` for a strictly greater
  answer and `<=` for greater-or-equal
  - Contribution problems usually make one boundary strict and the other
    non-strict so equal values do not count the same subarray twice
- Next-element answers become known when a candidate pops. Previous-element
  answers come from the nearest candidate that survives at the top
- A popped span has the arriving index as its right boundary and the new stack
  top as its left boundary, so its width is `right - left - 1`
- The algorithm takes `O(n)` time because each index is pushed once and popped at
  most once, while a monotonic input can require `O(n)` stack space
- Monotonic deques add a separate expiry rule for moving windows and are taught
  with [window maximums and minimums](../../04_sliding_window/notes/04_window_max_min.md)

## Interview Checklist

Before writing code, make sure you can answer each of these

```text
Is a later value settling an earlier unresolved value?
Do I need next or previous, and greater or smaller?
Should the stack be increasing or decreasing from bottom to top?
What does one entry represent, and do I need its index?
Does equality count, and should the pop comparison be strict?
When an entry pops, what answer or boundary becomes known?
What default should remain for entries that never pop?
For a span, do I read the left boundary after the pop?
Do equal values need asymmetric boundaries to avoid double counting?
Would a sentinel simplify draining the remaining candidates?
Can I justify O(n) by counting one push and at most one pop per index?
Does the problem involve a moving window, meaning expiry belongs to a deque?
```
