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

Sum Of Subarray Minimums adds those contributions. Sum Of Subarray Ranges runs
the idea once for maxima and once for minima, then subtracts. Maximal Rectangle
builds a histogram from every matrix row and reuses the rectangle routine.

## Variants In The Problem Set

The stack invariant stays useful even when the story changes:

- **Next Greater Element I** records next-greater answers in a map for a subset
  of queried values. **Next Greater Element II** scans `2 * n` positions with
  `i % n` to simulate a circular array, but pushes each real index only once
- **Online Stock Span** stores `(price, span)` and absorbs the spans of smaller or
  equal prices, so each `next()` call returns how far the current price dominates
  to the left
- **Trapping Rain Water** pops a valley when a right wall arrives, then uses the
  new stack top as the left wall. The popped height and distance determine the
  trapped layer
- **Remove K Digits** uses the stack as the answer under construction and pops a
  larger trailing digit while the deletion budget remains. **Remove Duplicate
  Letters** adds last-occurrence information so a character is removed only when
  it can still be used later
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

Scanning forward from every day is correct but quadratic on a decreasing input,
because each day searches the entire remaining forecast and finds nothing. A
monotonic stack keeps only the indices still waiting. Their temperatures decrease
from bottom to top, and a warmer day resolves all colder days at the top.

> “I’ll store indices because the answer is a distance. When day `i` is warmer
> than the day at index `j` on top, `i` is the first warmer day for `j`, so I pop
> `j` and write `i - j`. Equal temperatures stay because the problem says
> strictly warmer.”

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
