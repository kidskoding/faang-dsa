# XOR Patterns

## Pattern

XOR cancels equal values and preserves differences.

## Intuition

`a ^ a = 0` and `a ^ 0 = a`.

## How It Works

This makes XOR useful for single-number style problems.

## Template

```text
ans = 0
for x in nums:
    ans ^= x
return ans
```

## Example

In `[4,1,2,1,2]`, pairs cancel and `4` remains.

## Complexity

```text
Time: O(n)
Space: O(1)
```

## Pitfalls

- Using XOR when counts are not exactly paired.
- Forgetting XOR is order independent.
- Confusing XOR with exponentiation.

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
