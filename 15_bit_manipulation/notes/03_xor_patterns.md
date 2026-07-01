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
Do duplicates in this problem actually appear in cancelable pairs (or n-1 copies)?
Am I relying on `a ^ a = 0` and `a ^ 0 = a` correctly?
Does the order of XOR-ing elements matter here (it shouldn't)?
Would this problem break if a value appeared an odd number of times unintentionally?
```
