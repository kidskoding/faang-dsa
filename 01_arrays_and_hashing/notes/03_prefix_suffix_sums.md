# Prefix And Suffix Sums

## Pattern

Prefix sums store cumulative information from the left. Suffix sums store cumulative information from the right.

They let you answer range or split questions without recomputing sums repeatedly.

## Intuition

If you keep summing the same ranges over and over, precompute cumulative state once.

For sum from index `l` to `r`:

```text
prefix[r + 1] - prefix[l]
```

The extra leading zero makes empty prefix handling clean.

## How It Works

Build prefix sums:

```text
prefix[0] = 0
prefix[i + 1] = prefix[i] + nums[i]
```

Then any range sum is:

```text
sum(nums[l:r+1]) = prefix[r + 1] - prefix[l]
```

Suffix arrays work the same idea from the right.

## Template: Prefix Array

```text
prefix = [0]
for x in nums:
    prefix.append(prefix[-1] + x)
```

## Template: Running Prefix With Hash Map

```text
count = {0: 1}
running = 0
answer = 0

for x in nums:
    running += x
    answer += count.get(running - target, 0)
    count[running] = count.get(running, 0) + 1
```

This counts subarrays with sum equal to target.

## Example

For `nums = [2, 4, 1]`:

```text
prefix = [0, 2, 6, 7]
range sum 1..2 = prefix[3] - prefix[1] = 7 - 2 = 5
```

## Complexity

```text
build prefix: O(n)
range query: O(1)
space: O(n)
```

For running prefix without storing the whole array:

```text
time: O(n)
space: O(n) for the map
```

## Pitfalls

- Off-by-one errors with `prefix[r]` vs `prefix[r + 1]`.
- Forgetting `count[0] = 1` for subarrays starting at index 0.
- Using sliding window when negative numbers break the window logic.
- Not distinguishing prefix sum array from running prefix variable.

## Interview Checklist

Before coding, make sure you can answer:

```text
Am I indexing prefix[r] or prefix[r + 1] correctly for the range sum I need?
Did I seed count[0] = 1 for the running-prefix hash map variant?
Could negative numbers in the array break a sliding-window approach, requiring prefix sums instead?
Do I need a full prefix array (for repeated range queries) or just a running variable (for a single pass)?
Am I confusing the prefix sum array with the running prefix variable anywhere?
```
