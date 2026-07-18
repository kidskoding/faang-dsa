# Problem 2: Overnight Cutover

Robinhood's clearing system writes every executed trade into a nightly log,
ordered by strictly increasing trade ID. During last night's datacenter
cutover, the log file was split at an arbitrary point and the two halves
were reattached in the wrong order — the tail of the log now sits at the
front. No entries were lost or duplicated; the log is otherwise intact.

For example, a log that was originally

```text
[4012, 4155, 4300, 4477, 4512, 4890]
```

might have come out of the cutover as

```text
[4512, 4890, 4012, 4155, 4300, 4477]
```

Compliance needs to pull individual trades from this file all night, and the
file is far too large to re-sort. Given the post-cutover log `trades` and a
trade ID `target`, return the index of `target` in the log, or `-1` if no
such trade exists.

## Examples

### Example 1

```python
Input:
trades = [4512, 4890, 4012, 4155, 4300, 4477]
target = 4155

Output: 3
```

### Example 2

```python
Input:
trades = [4512, 4890, 4012, 4155, 4300, 4477]
target = 4600

Output: -1
```

### Example 3

```python
Input:
trades = [7001]
target = 7001

Output: 0
```

### Example 4

```python
Input:
trades = [4012, 4155, 4300]   # the split point happened to be at the very end
target = 4300

Output: 2
```

## Constraints

```text
1 <= len(trades) <= 10^5
0 <= trades[i], target <= 10^9
All trade IDs are unique
The log was originally strictly increasing, then split once and reattached
```

## Source

[LeetCode 33](https://leetcode.com/problems/search-in-rotated-sorted-array/)
