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

## What the Conversation Sounds Like

The [previous note](04_common_operation_costs.md) already explains the container
costs in this example. Here, the point is how a candidate moves through the
decisions without turning the interview into a speech.

> **Interviewer:** "Return whether a list of integers contains a repeated
> value."
>
> **Candidate:** "Can the list be empty, may I change it, and roughly how large
> can it be?"
>
> **Interviewer:** "It may be empty, do not change it, and assume it can be very
> large."
>
> **Candidate:** "Then `[4, 1, 4]` should return `True`, while `[4, 1, 7]` should
> return `False`. The direct approach compares each pair. That uses constant
> extra space but takes `O(n²)` time, which is too much for a large input because
> it repeatedly searches values it has already checked. I can keep the earlier
> values in a set instead, making one pass in `O(n)` average time and using
> `O(n)` extra space. Is that tradeoff acceptable?"
>
> **Interviewer:** "Yes. Go ahead and code it."
>
> **Candidate:** "I'll write the signature, create the set, and then scan the
> values. The important branch checks whether the current value was seen before
> I add it. After coding, I'll trace the repeated-value case, then check an empty
> list and a list with no repeat."
>
> **Candidate, after testing:** "The normal and boundary cases behave as
> expected. Let `n` be the list length. The scan is `O(n)` average time because
> each set operation is `O(1)` average case, and the set uses `O(n)` auxiliary
> space because it may hold every value."

The exchange is short, but it exposes the contract, a concrete example, the
correct brute force, its bottleneck, the optimization and its tradeoff, the plan
for code, the tests, and the final complexity. The algorithm details stay in the
note that teaches container costs.

## Narrate Decisions While You Code

Once the approach is agreed upon, write the signature and the important state.
Narrate decisions, not every character you type. One sentence before each
meaningful chunk is enough: what the state represents, what the loop maintains,
and what makes a branch return or continue.

The fact that must remain true while the code runs is an **invariant**. State it
in ordinary language before the loop, since that gives both you and the
interviewer something concrete to check. Prefer direct names such as `seen`,
`left`, `total`, or `node`. Add a helper only when it owns repeated logic.

## Test the Decisions, Not Just the Sample

Do not say "looks good" after coding. Trace one normal case through the important
state, then choose small inputs that challenge decisions in your code:

- Test the boundary, such as empty input or one item.
- Exercise the branch that returns an answer and the path that finds no answer.
- Include the special input property you clarified, such as duplicates or
  negative values.

Say what each test proves. A long random input is less informative than a tiny
case that reaches the branch most likely to be wrong.

## Keep Talking When You Are Stuck

Being stuck is recoverable; going silent removes the interviewer's ability to
help. Return to evidence you already have:

1. Restate what the output must represent.
2. Solve the smallest nontrivial example by hand.
3. State the correct brute force, even if it is slow.
4. Identify exactly which work the brute force repeats.
5. Ask which stored information would avoid that repetition.

If the interviewer gives a hint, acknowledge what changed:

> "That suggests I should keep a summary of the earlier values instead of
> rebuilding it each time. Let me update the state I am maintaining."

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

Describe the bug before editing. "This index can reach the list length, so I
will tighten the loop boundary" is better than changing several lines and
hoping.

## Handle Follow-Ups from the Existing Solution

An interviewer may change a constraint after the first solution. Start from the
tradeoff you already stated:

- If extra memory is no longer allowed, revisit the approach that spent memory
  to save time.
- If the input can no longer be changed, identify whether your solution mutates
  it and whether making a copy changes the space bound.
- If the return value changes from one answer to every answer, identify whether
  an early return or stored state must change.

Explain what remains valid and what must change. Do not discard working code
until the new requirement actually requires another approach.

## Summary

- A live interview is a conversation that moves from a clear contract to an
  example, a correct brute force, its bottleneck, an improved approach, code,
  tests, and complexity.
- The brute force is valuable when its repeated work leads directly to the state
  or tradeoff used by the better solution.
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
