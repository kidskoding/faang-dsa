# Linked List Basics

## Pattern

A linked list stores nodes connected by pointers instead of contiguous indices.

## Intuition

You move by following `next`; there is no O(1) random access by index.

## How It Works

Most bugs are pointer-order bugs. Save references before overwriting links.

## Template

```text
curr = head
while curr:
    process curr.val
    curr = curr.next
```

## Example

To remove a node, link the previous node around it.

## Complexity

```text
access by index: O(n)
insert/delete with node reference: O(1)
traversal: O(n)
```

## Pitfalls

- Losing the rest of the list by overwriting `next` too early.
- Forgetting dummy nodes simplify head deletion.
- Assuming list length is known.

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
