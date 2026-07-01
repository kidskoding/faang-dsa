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
Why does gcd(a, b) == gcd(b, a % b), and what breaks if I swap the arguments incorrectly?
What does my gcd function return when one input is 0, and is that the correct base case?
Am I computing `lcm` as `a // gcd(a, b) * b` (divide first) rather than `a * b // gcd(a, b)`, to avoid overflow in other languages?
Does my solution need gcd/lcm of more than two numbers, and do I fold pairwise correctly?
What is the time complexity of Euclid's algorithm in terms of log(min(a, b))?
```
