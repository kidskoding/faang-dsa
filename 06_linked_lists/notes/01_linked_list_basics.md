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
Do I need a reference to the node before the one I'm modifying, and have I saved it?
Would a dummy node before head remove a special case for deleting/inserting at the head?
Which pointer assignment, if made too early, would strand the rest of the list?
Am I relying on knowing the list length anywhere I shouldn't be?
Can I do this in O(1) space, or do I need extra structures (hash set, array)?
```
