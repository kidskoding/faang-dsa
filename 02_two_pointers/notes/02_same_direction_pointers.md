# Same-Direction Pointers

## Pattern

Use two pointers that both move left to right, often with one pointer writing or tracking a compressed result.

## Intuition

One pointer reads every value. The other pointer marks where the next valid value should go.

## How It Works

This is common for removing duplicates, filtering values, and compacting arrays in place.

## Template

```text
write = 0
for read in range(len(nums)):
    if nums[read] should be kept:
        nums[write] = nums[read]
        write += 1

return write
```

## Example

For remove duplicates, `read` scans every element while `write` only advances when a new unique value is accepted.

## Complexity

```text
Time: O(n)
Space: O(1)
```

## Pitfalls

- Incrementing `write` before assigning.
- Returning the array instead of the new logical length when the problem asks for length.
- Forgetting sorted input is often required for duplicate compaction.

## Interview Checklist

Before coding, make sure you can answer:

```text
What does `write` represent — the next free slot, or the last committed slot?
What is the "should be kept" condition for `read`, and does it depend on prior state (e.g. comparing to `nums[write - 1]`)?
Does `read` ever need to move faster than one step per iteration, or is it always a simple `for` loop?
Do I increment `write` before or after writing to `nums[write]`, and why?
Is `write` itself the answer (a count/length), or do I need to return `nums[:write]`?
Does the problem require sorted input for correctness, or does it work on arbitrary order?
```
