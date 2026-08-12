# Kadane's Algorithm

A **subarray** is a contiguous slice of an array. You may choose where it starts
and ends, but you may not skip a value in between. That makes "find the maximum
subarray sum" look like a boundary problem: there are `O(n²)` start/end pairs,
and adding each slice from scratch would do even more repeated work.

**Kadane's algorithm** removes the boundaries from the state. As you scan each
value, keep the best sum of a subarray that must end exactly here. That local
answer can either extend the previous local answer or restart at the current
value. A second variable keeps the best answer seen anywhere.

```text
current = best sum of a nonempty subarray ending at this index
best    = best sum of a nonempty subarray ending anywhere seen so far
```

## Extend the Previous Answer or Restart Here

At value `x`, there are only two candidates for `current`:

```text
restart: x
extend:  previous_current + x
```

Any worse subarray ending at the previous index is irrelevant. Appending the
same `x` preserves the difference between two candidate sums, so only the better
previous candidate can ever help later.

This gives one line:

```text
current = max(x, current + x)
```

If `current + x` loses, the entire previous subarray is rejected. Its sum hurts
the new subarray more than starting fresh at `x`.

Do not initialize the answer to zero unless an empty subarray is allowed. The
usual Maximum Subarray problem requires at least one value, so zero would invent
an invalid answer for `[-8, -3, -6]`.

```python
def max_subarray(nums: list[int]) -> int:
    if not nums:
        raise ValueError("max_subarray requires a nonempty array")

    current = nums[0]
    best = nums[0]

    for value in nums[1:]:
        current = max(value, current + value)
        best = max(best, current)

    return best


assert max_subarray([5]) == 5
assert max_subarray([-8, -3, -6]) == -3
```

`current` and `best` are different questions. The best subarray overall may end
before the scan does, so returning `current` is wrong. For `[5, -1, -10]`, the
final local answer is `-6`, but the global answer remains `5`.

## Worked Example: [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

Given a nonempty integer array, return the largest possible sum of a nonempty
contiguous subarray. Negative values are allowed, and the problem asks for the
sum rather than the indices.

Enumerating every pair of boundaries and maintaining a running sum for each
start takes `O(n²)` time. The repeated work is that many candidates arrive at
the same index, even though only the largest of them can help an extension.
Kadane keeps exactly that one useful candidate.

> "I will track the best subarray that must end at the current index. For each
> value I either extend that subarray or reject it and restart here. A separate
> global maximum remembers an answer that ended earlier."

```python
def max_subarray(nums: list[int]) -> int:
    if not nums:
        raise ValueError("max_subarray requires a nonempty array")

    current = nums[0]
    best = nums[0]

    for value in nums[1:]:
        current = max(value, current + value)
        best = max(best, current)

    return best


assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert max_subarray([-4, -2, -7]) == -2
assert max_subarray([9]) == 9
```

- **Time Complexity:** `O(n)`, where `n` is the array length, because each value
  is processed once with constant work.
- **Space Complexity:** `O(1)` auxiliary space, because only `current` and `best`
  are retained.

The trace shows both kinds of rejection:

```text
value   restart   extend   accepted current   best
-2       -2         --          -2             -2
 1        1         -1           1              1   reject extension
-3       -3         -2          -2              1   reject restart
 4        4          2           4              4   reject extension
-1       -1          3           3              4
 2        2          5           5              5
 1        1          6           6              6
-5       -5          1           1              6
 4        4          5           5              6   global 6 remains
```

The answer `6` comes from `[4, -1, 2, 1]`. The last row explains why both
variables are necessary: `current` becomes `5`, but that local candidate is
rejected as the global answer because an earlier subarray was better.

## Recovering the Winning Boundaries

If the interviewer asks for the subarray itself, remember where the current
candidate began. Restarting at index `i` resets `candidate_start` to `i`.
Whenever `current` improves `best`, copy the candidate's boundaries into the
answer boundaries.

```python
def max_subarray_with_indices(nums: list[int]) -> tuple[int, int, int]:
    if not nums:
        raise ValueError("max_subarray_with_indices requires a nonempty array")

    current = best = nums[0]
    candidate_start = best_start = best_end = 0

    for index in range(1, len(nums)):
        value = nums[index]
        if value > current + value:
            current = value
            candidate_start = index
        else:
            current += value

        if current > best:
            best = current
            best_start = candidate_start
            best_end = index

    return best, best_start, best_end


assert max_subarray_with_indices([-2, 1, -3, 4, -1, 2, 1]) == (6, 3, 6)
assert max_subarray_with_indices([-3]) == (-3, 0, 0)
```

On a tie, this version keeps the earlier answer because both comparisons use
`>` rather than `>=`. That is a deliberate tie rule; clarify it if the problem
requires the shortest, longest, earliest, or latest winning subarray.

## The Same Local-and-Global Shape

Kadane is one example of a broader scan: maintain the best state that must end
here, then update the best state seen anywhere. The workbook variations change
what the local state must remember.

### Running Minimum for One Stock Transaction

[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
asks for one buy before one later sell. At each price, the only earlier fact that
matters is the smallest price seen so far. The candidate profit is
`price - minimum_price`.

```python
def max_profit(prices: list[int]) -> int:
    if not prices:
        return 0

    minimum_price = prices[0]
    best = 0

    for price in prices[1:]:
        minimum_price = min(minimum_price, price)
        best = max(best, price - minimum_price)

    return best


assert max_profit([7, 1, 5, 3, 6, 4]) == 5
assert max_profit([7, 6, 4, 3, 1]) == 0
assert max_profit([]) == 0
```

A price is rejected as a sell when its profit is below `best`, but it can still
become the new buying minimum for later prices. Updating the minimum first also
allows same-day profit zero, which cannot incorrectly beat a positive result.

### Track Both Extremes When Signs Can Flip

For [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/),
a negative value reverses the ordering: the most negative product can become the
largest positive product. Therefore the local state needs both the maximum and
minimum product ending here.

```python
def max_product_subarray(nums: list[int]) -> int:
    if not nums:
        raise ValueError("max_product_subarray requires a nonempty array")

    current_max = current_min = answer = nums[0]

    for value in nums[1:]:
        from_max = current_max * value
        from_min = current_min * value
        current_max = max(value, from_max, from_min)
        current_min = min(value, from_max, from_min)
        answer = max(answer, current_max)

    return answer


assert max_product_subarray([2, 3, -2, 4]) == 6
assert max_product_subarray([-2, 3, -4]) == 24
assert max_product_subarray([-2, 0, -1]) == 0
```

Do not update `current_max` and then use that new value to compute
`current_min`; both new states must come from the same old pair. Saving
`from_max` and `from_min` prevents that accidental reuse.

### Max and Min Reveal Circular and Absolute Answers

For [Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/),
the winning values either do not wrap, which ordinary Kadane finds, or they wrap
around the ends. A wrapped answer keeps the total array except one middle
minimum-sum subarray, so its sum is `total - minimum_subarray`.

If every value is negative, the minimum subarray is the whole array and removing
it would create an empty answer. Reject the wrapped candidate in that case and
return the ordinary maximum, which is the least negative value.

[Maximum Absolute Sum of Any Subarray](https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/)
also runs the scan in both directions: find the maximum subarray sum and the
minimum subarray sum, then compare `maximum` with `-minimum`.

### Change the Meaning of "Extend"

In [Longest Turbulent Subarray](https://leetcode.com/problems/longest-turbulent-subarray/),
the local state is a run length rather than a sum. Keep `up` and `down`: an
increase extends the previous decreasing run, a decrease extends the previous
increasing run, and equality rejects both extensions and resets them to one.

[K-Concatenation Maximum Sum](https://leetcode.com/problems/k-concatenation-maximum-sum/)
repeats an array `k` times. Kadane over at most two copies captures the best
prefix and suffix connection. If the whole-array total is positive, every
middle copy can be accepted in full; otherwise those middle copies are rejected
because they cannot improve the sum. Returning `answer % 1_000_000_007` is an
output-format rule from the problem, not part of the local-state reasoning.

## Time and Space Complexity

| Approach                        | Time                                                                  | Space                                                                       |
| ------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Enumerate every start and end   | `O(n²)`: each of `O(n²)` boundary pairs is updated with a running sum | `O(1)` auxiliary: only boundaries, a running sum, and the answer are stored |
| Kadane's algorithm              | `O(n)`: each value performs one extend-or-restart decision            | `O(1)` auxiliary: the local and global states have fixed size               |
| Kadane with returned boundaries | `O(n)`: boundary bookkeeping adds constant work per value             | `O(1)` auxiliary: a fixed number of indices is retained                     |
| Maximum product variation       | `O(n)`: each value updates the local minimum and maximum once         | `O(1)` auxiliary: only two local extremes and one global answer are stored  |

## Summary

- Kadane's algorithm keeps the best nonempty subarray that must end at the
  current index and the best nonempty subarray found anywhere so far.
- The local transition chooses between restarting at the current value and
  extending the previous local answer. The losing candidate is discarded
  because it can never become better after receiving the same future values.
- Initialize from the first element when the subarray must be nonempty, because
  initializing to zero gives a false answer on an all-negative array.
- `current` answers a local question and `best` answers a global one, so returning
  the final `current` can lose an answer that ended earlier.
- The same scan shape can track a running minimum for stock profit, both product
  extremes for sign flips, or both maximum and minimum sums for circular and
  absolute-sum variants.
- Recovering indices requires one candidate start and one saved winning range;
  tie behavior follows from choosing `>` or `>=` in the update branches.

## Interview Checklist

```text
Is the answer a contiguous subarray, and must it be nonempty?
What does the local state represent at exactly the current index?
What are the restart and extend candidates?
Why can the losing local candidate never help later?
Am I keeping a separate global answer that may have ended earlier?
Does all-negative input rule out initialization to zero?
Do sign flips require both a local minimum and maximum?
If I return indices, what tie rule does the problem require?
For a circular answer, have I rejected the empty wrapped case?
```
