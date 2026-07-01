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
Am I building a prefix/failure table (KMP) or a Z-array, and what does each entry mean?
Why does the text pointer never move backward, only the pattern pointer via the fallback table?
On a mismatch, how does the table tell me how much matched prefix I can safely reuse?
Is the table built on the pattern alone, or on pattern+separator+text (Z-algorithm)?
Would a simpler hash-based or built-in substring check meet the requirement instead?
```
