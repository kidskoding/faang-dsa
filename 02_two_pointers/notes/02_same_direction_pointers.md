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
What pattern is this?
What state or invariant am I maintaining?
What is the base case or initialization?
When do I update the answer?
Why is the movement/transition valid?
What is the time and space complexity?
```
