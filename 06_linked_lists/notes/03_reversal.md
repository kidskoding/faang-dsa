# Linked List Reversal

## Pattern

Reverse links one at a time while walking the list.

## Intuition

At each node, point it backward to the previous node, then advance.

## How It Works

You need `next_node` saved before changing `curr.next`.

## Template

```text
prev = None
curr = head
while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
return prev
```

## Example

For `1->2->3`, after processing `2`, the partial reversed list is `2->1`.

## Complexity

```text
Time: O(n)
Space: O(1)
```

## Pitfalls

- Forgetting to save `next`.
- Returning old head instead of `prev`.
- Breaking the list during sublist reversal.

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
