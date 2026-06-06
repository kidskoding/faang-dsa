# Interview Problem Solving

## Goal

Build a repeatable live-coding process so you do not jump straight into code without understanding the problem.

## The Loop

1. Restate the problem.
1. Clarify inputs, outputs, constraints, and edge cases.
1. Work through one small example.
1. Name the likely pattern.
1. Explain the approach before coding.
1. Code cleanly.
1. Test normal cases, edge cases, and failure cases.
1. Analyze time and space complexity.

## Before Coding

Ask:

```text
Can the input be empty?
Are duplicates allowed?
Are values negative?
Is the input sorted?
Can I mutate the input?
What should happen if no answer exists?
```

## While Coding

- Keep variable names direct.
- Prefer small helper functions for recursion.
- Handle base cases first.
- Do not optimize before the basic logic is correct.
- Say what each major block is doing out loud.

## After Coding

Test:

```text
empty input
single item
normal case
duplicates
negative values
already sorted / reverse sorted
missing answer
largest likely shape
```

Then explain:

```text
Let n be ______.
Time is O(____), because ______.
Space is O(____), because ______.
```

## Debugging

If a solution fails:

1. Re-run the smallest failing example by hand.
1. Check base cases.
1. Check pointer movement or recursion return values.
1. Check whether you are losing information.
1. Check whether the data structure contains the right thing.

For trees and graphs, be especially careful about whether your queue/stack contains nodes, values, coordinates, or state tuples.
