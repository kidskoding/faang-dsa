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
Am I applying `% m` after every addition/multiplication, not just at the end?
Could an intermediate value go negative, and does my language's `%` handle that the way I expect?
Is `m` prime, and do I need modular inverse (pow(a, m-2, m)) instead of division?
Am I using modulo for cyclic indexing (wraparound) versus needing an exact, un-modded value somewhere?
Why does `(a + b) % m == ((a % m) + (b % m)) % m` hold, and does the same identity hold for multiplication in my code?
What is the time and space complexity per operation?
```
