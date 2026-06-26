# Merge And Split

## Pattern

Merge sorted lists by choosing the smaller head; split lists with fast/slow.

## Intuition

Dummy nodes make merge logic cleaner because the output head is not special.

## How It Works

For divide-and-conquer list problems, split, solve halves, then merge.

## Template

```text
dummy = Node(0)
tail = dummy
while a and b:
    attach smaller node to tail
    advance tail
attach remaining list
return dummy.next
```

## Example

Merging `1->4` and `2->3` picks `1`, then `2`, then `3`, then `4`.

## Complexity

```text
Time: O(n)
Space: O(1) for iterative merge
```

## Pitfalls

- Creating new nodes when relinking existing nodes is enough.
- Forgetting to attach the remainder.
- Not cutting the first half when splitting.

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
