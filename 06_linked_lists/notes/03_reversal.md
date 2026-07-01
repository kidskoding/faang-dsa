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
Have I saved `curr.next` before overwriting `curr.next = prev`?
What do I return at the end — `prev` or `curr` — and why is that the correct new head?
If reversing only a sublist, what nodes do I need references to before and after the sublist to reconnect it?
What are `prev` and `curr` pointing to at the top of each loop iteration — is that invariant true before the first iteration too?
What is the time and space complexity, and could I do this recursively instead — what would the space tradeoff be?
```
