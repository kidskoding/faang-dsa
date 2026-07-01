# Masks

## Pattern

A mask selects or modifies specific bits.

## Intuition

Think of a mask as a set of bit positions.

## How It Works

Use AND to test, OR to set, XOR to toggle.

## Template

```text
is_set = x & (1 << i)
set_bit = x | (1 << i)
clear_bit = x & ~(1 << i)
toggle = x ^ (1 << i)
```

## Example

Bit `i` is represented by `1 << i`.

## Complexity

```text
O(1) per bit operation
Space O(1)
```

## Pitfalls

- Off-by-one bit positions.
- Using decimal intuition instead of binary.
- Forgetting parentheses around shifts.

## Interview Checklist

Before coding, make sure you can answer:

```text
Am I testing, setting, clearing, or toggling a bit?
Does `1 << i` correctly line up with the bit position I mean?
Did I parenthesize the shift so it isn't swallowed by AND/OR/XOR precedence?
For clearing a bit, did I use `~(1 << i)` and not `~1 << i`?
```
