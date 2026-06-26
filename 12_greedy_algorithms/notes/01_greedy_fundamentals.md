# Greedy Fundamentals

## Pattern

Greedy makes the locally best choice and commits to it.

## Intuition

It works only when local choices can be proven to lead to a global optimum.

## How It Works

The key skill is justification, not just guessing.

## Template

```text
sort or scan input
maintain current best local choice
commit when safe
return accumulated answer
```

## Example

Choosing earliest finishing interval leaves maximum room for future intervals.

## Complexity

```text
Usually O(n) or O(n log n) if sorting is needed
Space often O(1) or O(n)
```

## Pitfalls

- Using greedy without proof.
- Choosing the wrong local rule.
- Missing counterexamples.

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
