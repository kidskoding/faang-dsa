# Solving a Problem in a Live Interview

A live-coding interview is a conversation in which code is one piece of
evidence. The interviewer needs to see how you remove ambiguity, compare
approaches, turn an idea into code, and check your own work. A correct solution
that appears after a long silence hides most of that evidence.

Use one connected loop:

```text
clarify -> example -> brute force -> bottleneck -> optimize -> code -> test -> analyze
```

You do not need to announce these as eight formal steps. The goal is a natural
conversation in which the next decision follows from the previous one.

## Clarify the Contract Before Choosing an Algorithm

Restate the task in your own words, then ask only questions that could change the
solution or its code. Useful questions often concern:

- the input and exact return value;
- empty input, duplicates, negative values, or missing answers;
- whether the input is sorted or may be mutated;
- the expected input size and memory limits;
- what to do when several valid answers exist.

Avoid asking facts already stated in the prompt merely to fill time. If the
interviewer says to make a reasonable assumption, state it and continue:

> "I'll assume the input can be empty and that I should return `False` when it
> contains fewer than two values. I'll leave the input unchanged."

Walk through one small example before coding. A concrete example often exposes
an ambiguity faster than another abstract question.

## Let the Brute Force Reveal the Better Approach

The first solution does not need to be fast. It needs to be correct and useful.
State the straightforward approach, derive its cost, and name the repeated work
that makes it too slow for the constraints.

Suppose the prompt is:

> Given a list of integers, return `True` if any value appears at least twice.

For `[4, 1, 4]`, the answer is `True`; for `[4, 1, 7]`, it is `False`. A direct
approach compares every pair. That is correct, but it examines up to
`n(n - 1) / 2` pairs, so it takes `O(n²)` time.

The repeated work is searching the earlier values again for every new value.
The [Python container costs](04_common_operation_costs.md) suggest the repair: a
set answers whether a value has already appeared in `O(1)` average time.

> "I can trade `O(n)` extra space for `O(n)` average time by storing the values
> already seen. Before adding each value, I'll check whether it is in the set."

That explanation gives the interviewer the brute force, bottleneck, tradeoff,
and invariant. The **invariant** is the fact that remains true while the
algorithm runs: before processing the current value, `seen` contains exactly the
values processed earlier.

## Code in Explainable Chunks

Once the approach is agreed upon, write the signature and the important state.
Narrate decisions, not every character you type.

```python
def contains_duplicate(nums: list[int]) -> bool:
    seen: set[int] = set()

    for value in nums:
        if value in seen:
            return True
        seen.add(value)

    return False


assert contains_duplicate([4, 1, 4]) is True
assert contains_duplicate([4, 1, 7]) is False
assert contains_duplicate([]) is False
assert contains_duplicate([-2, -2]) is True
```

Useful narration here is short:

> "The set starts empty. If the current value is already present, I have found
> the required pair and can return immediately. Otherwise I add it. If the loop
> finishes, every processed value was new, so I return `False`."

The order of the check and insertion matters. Adding first would make every
value look like a duplicate of itself. Explain that branch when you write it;
do not wait for the interviewer to discover why it is there.

Prefer direct names such as `seen`, `left`, `window_sum`, or `node`. Add a helper
when it owns repeated logic or a recursive contract. Avoid polishing unrelated
syntax while the core solution is still incomplete.

## Test the Decisions, Not Just the Sample

Do not say "looks good" after coding. Trace a normal case through the important
state, then choose edge cases that challenge decisions in your code.

For `[4, 1, 4]`:

```text
value=4   seen={}       not present, add it       seen={4}
value=1   seen={4}      not present, add it       seen={1, 4}
value=4   seen={1, 4}   present, return True
```

Then test the boundaries:

- `[]` and `[7]` both finish the loop and return `False`.
- `[-2, -2]` confirms that negative values need no special treatment.
- `[3, 3, 3]` confirms that the first repeated occurrence returns immediately.

These tests are useful because they exercise the empty path, the no-answer path,
and the early-return branch. A long random input is less informative to trace by
hand.

Finally volunteer the analysis:

> "Let `n` be the number of values. I visit each value once and do an average
> `O(1)` set lookup and insertion, so the time is `O(n)` average case. The set
> can hold all `n` distinct values, so the auxiliary space is `O(n)`."

The word "average" is important because set operations have a theoretical
collision-heavy `O(n)` worst case.

## Keep Talking When You Are Stuck

Being stuck is recoverable; going silent removes the interviewer's ability to
help. Return to evidence you already have:

1. Restate what the output must represent.
2. Solve the smallest nontrivial example by hand.
3. State the correct brute force, even if it is slow.
4. Identify exactly which work the brute force repeats.
5. Ask which stored information would avoid that repetition.

If the interviewer gives a hint, acknowledge what changed:

> "That suggests I should store previous prefix sums rather than only the
> current window. Let me update the state I am maintaining."

Do not defend an old approach after its assumption has failed. Incorporating a
hint cleanly is useful signal because real engineering also involves revising a
plan from new information.

When code fails, run the smallest failing case line by line. Inspect state where
it first differs from what you expected. Common checks include:

- Does a pointer always move, or can the loop repeat forever?
- Does the base case return the correct type and value?
- Did mutation happen before or after the value was needed?
- Does a queue, stack, heap, or set store the full state needed later?
- Is an index allowed to reach `len(values)`, or must it stop before it?

Describe the bug before editing. "This check happens after the insertion, so the
current value matches itself; I will move the check before the insertion" is
better than changing several lines and hoping.

## Handle Follow-Ups from the Existing Solution

An interviewer may change a constraint after the first solution. Start from the
tradeoff you already stated:

- If extra space is no longer allowed, the set solution may not fit; sorting
  could group duplicates in `O(n log n)` time with different mutation or copy
  costs.
- If values arrive as a stream, the set logic still works, but memory grows with
  the number of distinct values seen.
- If the interviewer asks for duplicate counts rather than existence, a
  dictionary replaces the set because each key now needs an associated count.

Explain what remains valid and what must change. Do not discard working code
until the new requirement actually requires another approach.

## Summary

- A live interview is a conversation that moves from a clear contract to an
  example, a correct brute force, its bottleneck, an improved approach, code,
  tests, and complexity.
- The brute force is valuable when its repeated work leads directly to the data
  structure or invariant used by the better solution.
- Narrate decisions and tradeoffs rather than every line of syntax, and state the
  invariant before the loop that maintains it.
- Test branches and boundaries with small inputs, because they reveal more than
  rerunning only the provided sample.
- When stuck or debugging, expose the smallest failing state and revise the
  specific assumption that failed.

## Interview Checklist

```text
Can I restate the exact input, output, and ambiguous behavior?
Have I walked through one small example?
What is the simplest correct approach?
Which repeated work or constraint makes that approach insufficient?
What state or invariant removes the bottleneck?
Can I explain each important branch before I code it?
Which normal case, boundary, and failure branch will I test?
Can I derive time and auxiliary space with named variables?
If I receive a hint or follow-up, can I state what changed?
```
