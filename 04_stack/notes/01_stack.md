# Stack

## Pattern

A stack is last-in, first-out. The most recent item is processed first.

## Intuition

Use a stack when nested, reversed, or pending work needs to be resolved later.

## How It Works

Stacks appear in parsing, matching parentheses, DFS, expression evaluation, and undo-like behavior.

## Template

```text
stack = []
for x in items:
    if should_push(x):
        stack.append(x)
    else:
        top = stack.pop()
```

## Example

For valid parentheses, push opening brackets and pop when a matching closing bracket appears.

## Complexity

```text
push/pop/top: O(1)
space: O(n)
```

## Pitfalls

- Popping from an empty stack.
- Forgetting to check the stack is empty at the end.
- Using a stack when order should be FIFO.

## Interview Checklist

Before coding, make sure you can answer:

```text
Does this problem have nested, reversed, or "most recent unresolved" structure that maps to LIFO order?
What exactly gets pushed: the raw value, an index, or a (value, extra) tuple?
What condition triggers a pop, and what do I do with the popped item?
Is the stack guaranteed to be empty at the end, or does leftover content signal something (e.g. unmatched brackets)?
Could this be solved without a stack, e.g. with two pointers or a counter, more simply?
```
