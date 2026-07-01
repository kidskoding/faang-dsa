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
What is the greedy rule (local choice) I am claiming is optimal?
Can I prove it with an exchange argument, or find a counterexample first?
Does the input need sorting to make the greedy choice well-defined, and by what key?
What accumulated state am I carrying forward as I commit to each choice?
If I can't justify why the local choice can never be beaten later, should this be DP instead?
```
