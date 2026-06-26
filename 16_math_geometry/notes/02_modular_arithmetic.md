# Modular Arithmetic

## Pattern

Modulo keeps numbers inside a fixed range and models wraparound.

## Intuition

Use modulo for cyclic indexing, large counts, and arithmetic under constraints.

## How It Works

Common identity: `(a + b) % m = ((a % m) + (b % m)) % m`.

## Template

```text
next_index = (i + 1) % n
value = (value * base + digit) % mod
```

## Example

Clock arithmetic wraps after 12; arrays wrap after n.

## Complexity

```text
O(1) per operation
Space O(1)
```

## Pitfalls

- Negative modulo behavior differs by language.
- Forgetting modulo after multiplication.
- Using modulo when exact value is needed.

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
