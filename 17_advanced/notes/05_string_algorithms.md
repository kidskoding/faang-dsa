# KMP And Z Algorithm

## Pattern

Advanced string algorithms avoid rechecking characters after partial matches.

## Intuition

They precompute how much prefix information can be reused.

## How It Works

Use when repeated pattern matching must be linear.

## Template

```text
build prefix table
scan text using table to skip fallback comparisons
```

## Example

KMP matches a pattern in text without moving the text pointer backward.

## Complexity

```text
Time O(n+m)
Space O(m)
```

## Pitfalls

- Trying to memorize without understanding prefix reuse.
- Using advanced string algorithms when simple hash/trie is enough.
- Off-by-one prefix table bugs.

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
