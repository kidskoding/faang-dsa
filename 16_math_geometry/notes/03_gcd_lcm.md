# GCD And LCM

## Pattern

GCD finds greatest common divisor; LCM finds least common multiple.

## Intuition

Euclid works because gcd(a,b) = gcd(b, a % b).

## How It Works

LCM can be computed from gcd.

## Template

```text
def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
lcm = a // gcd(a,b) * b
```

## Example

gcd(20, 12) -> gcd(12, 8) -> gcd(8, 4) -> 4.

## Complexity

```text
gcd: O(log min(a,b))
space: O(1)
```

## Pitfalls

- Computing lcm as `a*b` before dividing and overflowing in other languages.
- Not handling zero carefully.
- Confusing divisor with multiple.

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
