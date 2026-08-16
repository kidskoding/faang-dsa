# Fixed-Size Sliding Window

A **window** is one contiguous part of an array or string. **Contiguous** means
the elements sit next to one another, so a window cannot skip from index 1 to
index 4. A **fixed-size window** always contains exactly `k` elements, where the
problem gives you `k` before the scan begins.

For `nums = [1, 12, -5, -6, 50, 3]` and `k = 4`, there are three windows:

```text
nums     1   12   -5   -6   50    3
        [-----------------]             sum = 2
             [------------------]       sum = 51
                  [------------------]  sum = 42
```

The first and second windows share `12, -5, -6`. Sliding right changes only two
things: `50` enters at the right and `1` leaves at the left. A fixed window
reuses the other `k - 1` elements rather than processing them again.

This is the first important contrast in the module:

- A **fixed-width** problem states the size, such as "a substring of length
  `k`". Both boundaries move together.
- A [**variable-width** problem](02_variable_size_window.md) states a condition,
  such as "no repeated characters". The boundaries move independently, and the
  width is part of the answer.

## Add One And Drop One

Summing every slice separately is correct, but it costs `O(n * k)` because each
of the roughly `n` windows reads `k` values. The overlap above gives the better
update:

```text
new window state = old state + entering contribution - leaving contribution
```

For example, Maximum Average Subarray I asks for the largest average among all
windows of width `k`. Every candidate uses the same divisor, so maximizing the
sum also maximizes the average. Divide only after finding the best sum.

```python
def find_max_average(nums: list[int], k: int) -> float:
    window_sum = sum(nums[index] for index in range(k))
    best_sum = window_sum

    for right in range(k, len(nums)):
        window_sum += nums[right] - nums[right - k]
        best_sum = max(best_sum, window_sum)

    return best_sum / k


assert find_max_average([1, 12, -5, -6, 50, 3], 4) == 12.75
assert find_max_average([5], 1) == 5.0
assert find_max_average([-3, -1, -4], 2) == -2.0
assert find_max_average([4, 0, 4, 0], 4) == 2.0
```

The first window is **primed** before the loop because there is no earlier
window to update. `right` then starts at `k`, the first index not already in that
window. When `right` enters, `right - k` leaves.

Seed `best_sum` with the first real sum rather than `0`. On all-negative input,
zero is not a candidate and would incorrectly beat every window. When `k = 1`,
priming uses the first value and every later step replaces exactly that one
value, so the same code still works.

The running state does not have to be a sum. It only needs an `O(1)` way to add
the entering element and undo the leaving element:

- Maximum Number of Vowels in a Substring of Given Length keeps a count. Add
  one when the entering character is a vowel and subtract one when the leaving
  character is a vowel.
- Number of Sub-arrays of Size K and Average Greater Than or Equal to Threshold
  keeps a sum and tests `window_sum >= k * threshold`. Multiplying the threshold
  avoids a floating-point division for every window.
- Substrings of Size Three with Distinct Characters keeps three character
  counts, or compares `len(set(s[i : i + 3]))` with 3 because the width is the
  constant 3.

Contains Duplicate II asks whether equal values occur at indices at most `k`
apart. Before checking index `right`, a set can hold the values at the previous
`k` positions. The order is important: evict the position that became too old,
check whether the new value is already present, and only then add it.

```python
def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    window: set[int] = set()

    for right, value in enumerate(nums):
        if right > k:
            window.discard(nums[right - k - 1])
        if value in window:
            return True
        window.add(value)

    return False


assert contains_nearby_duplicate([1, 2, 3, 1], 3) is True
assert contains_nearby_duplicate([1, 0, 1, 1], 1) is True
assert contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2) is False
assert contains_nearby_duplicate([1, 1], 0) is False
assert contains_nearby_duplicate([], 1) is False
```

The eviction is `right - k - 1`, not `right - k`, because the `k` positions
immediately before `right` are still close enough to match it. A set is safe in
this particular scan because the function returns as soon as a second live copy
is found. Windows that must continue after duplicates enter need the counts
taught in [frequency-map windows](03_frequency_map_windows.md).

## Separate What The Window Changes

Some fixed-window problems hide the window inside a larger answer.

Grumpy Bookstore Owner has customers who are already satisfied during calm
minutes and customers who could be saved during one `minutes`-long stretch. The
first group is a fixed `base`. Slide only over the second group, adding
`customers[i]` when minute `i` is grumpy and otherwise adding zero. The answer is
`base + best_saved_window`.

This split is useful whenever part of the answer is guaranteed and one fixed
stretch controls only the extra gain:

```text
answer = contribution that is always present + best change inside one window
```

## Worked Example: [Maximum Points You Can Obtain From Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/)

You are given card points in a row and must take exactly `k` cards. Every card
must come from the current left or right end. Return the largest possible score.

**Input**: `card_points`, a `list[int]` holding the points on each card in row
order, and `k`, an `int` giving exactly how many cards must be taken, where
`1 <= k <= len(card_points) <= 10^5` and every point value is between `1` and
`10^4`

**Output**: a single `int`, the largest total that any legal sequence of `k`
end-takes can reach. It is a maximum over choices, not the score of one
particular greedy sequence, and because every card is worth at least `1`, taking
all `n` cards is always allowed and returns the whole total

A tempting greedy choice is to take the larger exposed end each time. It fails
on `[1, 100, 3, 4, 5]` with `k = 2`: taking `5`, then `4`, scores 9, while
taking the small `1` exposes `100` and scores 101. A local end does not reveal
what it unlocks next.

The useful reframe is to look at what remains. After taking `k` cards from the
ends, the `n - k` cards not taken must form one contiguous middle block.
Therefore,

```text
maximum points taken = total points - minimum sum of a window of width n - k
```

> “Instead of deciding left or right `k` times, I will minimize the contiguous
> block left behind. Its width is fixed at `n - k`, so I can update its sum by
> adding one card and dropping one card on each slide.”

1. Compute `leftover_width = n - k`, because the cards you do not take are
   exactly the ones left in the middle, and their count is fixed the moment `k`
   is known. This is the width the window will hold for the whole scan.
2. Compute `total`, the sum of every card. The score you keep is whatever the
   total is minus whatever the middle block holds, so the total is the fixed
   part of the formula and only the block varies.
3. **Prime** the first window by summing the first `leftover_width` cards, which
   is the block left behind when all `k` cards are taken from the right end.
   There is no earlier window to update from, so this one has to be built
   directly. When `k` equals `n` the width is zero and this sum is `0`, which is
   the correct block for taking every card.
4. Seed `smallest` with that primed sum rather than with zero or infinity,
   because a real window is already in hand and it is a genuine candidate.
5. Slide `right` from `leftover_width` to the last index. On each step add
   `card_points[right]`, the card entering on the right, and subtract
   `card_points[right - leftover_width]`, the card falling off the left, so the
   `leftover_width - 1` shared cards are never re-added.
6. After each slide, keep `smallest = min(smallest, window_sum)`, since the
   answer depends on the best block seen anywhere in the scan and not on the
   block the loop happens to end on.
7. Return `total - smallest`. Each window position corresponds to one legal
   split of `k` cards between the two ends, so minimizing the block left behind
   maximizes the points taken

```python
def max_score(card_points: list[int], k: int) -> int:
    leftover_width = len(card_points) - k
    total = sum(card_points)
    window_sum = sum(card_points[index] for index in range(leftover_width))
    smallest = window_sum

    for right in range(leftover_width, len(card_points)):
        window_sum += card_points[right] - card_points[right - leftover_width]
        smallest = min(smallest, window_sum)

    return total - smallest


assert max_score([1, 2, 3, 4, 5, 6, 1], 3) == 12
assert max_score([2, 2, 2], 2) == 4
assert max_score([9, 7, 7, 9, 7, 7, 9], 7) == 55
assert max_score([1, 79, 80, 1, 1, 1, 200, 1], 3) == 202
```

For `[1, 2, 3, 4, 5, 6, 1]` and `k = 3`, the leftover width is 4:

```text
left behind [1,2,3,4]  sum=10  smallest=10  ACCEPT
left behind [2,3,4,5]  sum=14  smallest=10  REJECT
left behind [3,4,5,6]  sum=18  smallest=10  REJECT
left behind [4,5,6,1]  sum=16  smallest=10  REJECT

total=22, so the best score is 22 - 10 = 12
```

The rejected windows matter because they show that the answer remembers the
best state seen rather than trusting the final state. When `k` equals the array
length, `leftover_width` is zero. Every update adds and subtracts the same card,
so `smallest` stays zero and the function correctly returns the total without a
special case.

- **Time Complexity:** `O(n)`, because the total and the window scan each touch
  every one of the `n` cards a constant number of times.
- **Space Complexity:** `O(1)` auxiliary space, because the middle window is
  summarized by two integers rather than copied.

A useful follow-up scans only the `k + 1` possible left/right splits. Start with
the sum of the rightmost `k` cards, then replace one chosen card from the right
with one from the left on each step. That takes `O(k)` time and `O(1)` space, so
it is preferable when `k` is much smaller than `n`. The complement version above
is the clearer derivation of the fixed contiguous window.

## Fixed Window Or Prefix Sums

Both a sliding sum and a
[prefix sum](../../01_arrays_and_hashing/notes/03_prefix_suffix_sums.md) avoid
re-summing overlapping ranges. Use the structure that matches how the ranges
arrive:

| Situation                                        | Better fit                              | Reason                                                                                   |
| ------------------------------------------------ | --------------------------------------- | ---------------------------------------------------------------------------------------- |
| Visit every width-`k` range from left to right   | Fixed window                            | It updates in `O(1)` and needs only the running state.                                   |
| Answer arbitrary range queries later             | Prefix sums                             | The `O(n)` prefix array makes any requested range `O(1)`.                                |
| Need the maximum or minimum element after expiry | [Monotonic deque](04_window_max_min.md) | A sum can be subtracted, while an expired maximum cannot be recovered from one variable. |

## Time and Space Complexity

Let `n` be the input length and `k` the fixed width.

| Approach                   | Time                                                                     | Space                                                               |
| -------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| Recompute every window     | `O(n * k)`: each of `n - k + 1` starts reads all `k` elements again      | `O(1)` auxiliary space when the range is scanned without copying it |
| Running sum or count       | `O(n)`: each element enters once and leaves once                         | `O(1)`: a few numbers summarize the current window                  |
| Set or frequency-map state | `O(n)` average: each element performs average-constant-time hash updates | `O(k)`: at most one window of `k` elements is represented           |
| Card-pick split scan       | `O(k)`: each of the `k + 1` left/right splits changes one chosen card    | `O(1)`: one chosen-card sum is updated in place                     |

## Summary

- A **fixed-size sliding window** is a contiguous block whose width `k` is given
  before the scan begins. Both boundaries move right together, unlike a
  variable window whose condition decides the width.
- Recomputing all `k` elements at every start costs `O(n * k)`. Priming the
  first window and then adding the entering contribution while removing the
  leaving contribution reduces the scan to `O(n)`.
- When `right` is the new index, `right - k` leaves a normal width-`k` window.
  Derive that index from the range the window should contain instead of
  memorizing it.
- A sum or count uses `O(1)` space, while a set or map can use `O(k)` because it
  represents the actual contents of the window.
- A fixed window may describe only part of the answer. Grumpy Bookstore Owner
  adds a guaranteed base to the best extra gain, while Maximum Points From Cards
  minimizes the fixed-width middle block that is left behind.
- A running maximum does not support “subtract the leaving value.” Use a
  monotonic deque when an extreme must stay exact as the window moves.

## Interview Checklist

```text
Is the width given, or does a condition decide it?
Does the problem require one contiguous block rather than any k choices?
What does the first window contain, and how will I prime its state?
When right enters, which exact index leaves?
Can the state add and undo one contribution in O(1)?
Should best start from the first real window rather than from zero?
Is part of the answer fixed outside the window?
Is the chosen part easier to express through its contiguous complement?
What happens when k is 1 or k equals the input length?
```
