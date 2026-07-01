# In-Place Mutation

## Pattern

Modify the input array using pointer positions instead of allocating a new array.

## Intuition

Many interview problems require `O(1)` extra space. The trick is to separate read position from write position or swap targets into place.

## How It Works

The array may temporarily contain stale values beyond the returned length or outside the finalized region.

## Template

```text
write = 0
for read in range(n):
    if keep(nums[read]):
        nums[write] = nums[read]
        write += 1
```

## Example

After removing values, the part after `write` does not matter unless the problem explicitly asks for it.

## Complexity

```text
Time: O(n)
Space: O(1)
```

## Pitfalls

- Expecting removed values to disappear physically.
- Overwriting values before reading them.
- Not preserving relative order when the problem requires stability.

## Interview Checklist

Before coding, make sure you can answer:

```text
Am I about to overwrite `nums[write]` before I've finished reading its old value elsewhere?
Does the problem require preserving relative order, or can I swap-from-the-end instead?
What is left in the array beyond the final `write` index, and does the problem care?
Is `O(1)` extra space actually required, or would a new array make the solution simpler and still acceptable?
If I need to write from the back (e.g. merging two sorted arrays), why does moving right-to-left avoid overwriting unread values?
```
