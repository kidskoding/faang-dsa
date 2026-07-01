# Bitwise Basics

## Pattern

Bit operations manipulate integer binary representation directly.

## Intuition

They are useful for flags, parity, powers of two, and compact state.

## How It Works

Core operators: AND, OR, XOR, NOT, shifts.

## Template

```text
x & mask
x | mask
x ^ y
x << 1
x >> 1
```

## Example

`x & 1` checks whether x is odd.

## Complexity

```text
Usually O(1) per operation
Space O(1)
```

## Pitfalls

- Confusing logical and bitwise operators.
- Forgetting negative numbers are tricky in Python bit representation.
- Using bit tricks where clarity matters more.

## Interview Checklist

Before coding, make sure you can answer:

```text
Am I reasoning about bits as binary, not decimal?
Which operator (AND/OR/XOR/NOT/shift) matches the effect I want?
Does this problem involve negative numbers, and how does Python represent them?
Would a bit trick actually be clearer than a straightforward check here?
```
