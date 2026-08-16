# Timed Solving

A **time box** is a fixed amount of clock time assigned to one phase of work,
decided before the phase starts, together with a rule for what happens when that
time runs out. The rule is the part that matters. A budget with no consequence
attached is a wish, and it will be quietly overrun every time

You already keep **invariants**, which are facts you hold true about your program
state while a loop runs. A time box is the same discipline pointed at the clock
instead of the data: a fact you hold true about elapsed time, checked at fixed
moments, with a defined action when the check fails

The hook is a chess clock. A grandmaster who finds the winning move after
thinking for twenty minutes has not found a winning move, because the twenty
minutes are themselves part of the position. An interview works the same way. The
`O(n)` solution you reach at minute 30 of a 35-minute slot is worth less than the
`O(n * k)` solution you finished and tested at minute 20, because only one of them
gets to exist as running code

> This topic covers what the clock is actually grading, why a single deadline at
> the end gives you no usable feedback, the checkpoint schedule that replaces it,
> and the commit rule that fires when a checkpoint slips

## What The Clock Is Grading

The usual live-coding slot is 45 minutes, of which roughly 35 are yours: the rest
goes to introductions, the interviewer reading the problem out, and questions at
the end. In that window the interviewer needs to see a contract, an approach with
a stated tradeoff, code that runs, a test you performed rather than asserted, and
a complexity claim you can defend. All five, in the
[order that makes them a conversation](../../00_fundamentals/notes/05_interview_problem_solving.md)

Running out of time is not a small deduction against an otherwise strong
performance. It deletes the evidence entirely. An interviewer cannot write "would
have tested it" on a scorecard, so an untested solution scores as untested, and a
half-typed optimal solution scores as no solution

Two things this is not:

- It is not typing speed. Nobody has ever failed a loop because they type 60
  words per minute instead of 90. Time is lost in the two places where you are not
  typing at all, which are deriving an approach you cannot finish and debugging
  code you never traced
- It is not the [online assessment](../../00_fundamentals/notes/01_how_to_prep.md),
  where you are alone with a submit button and the right move is to bank the
  easiest points across the whole set. Here there is one problem and a person
  watching, so the currency is visible progress rather than throughput

## Why One Deadline At The End Tells You Nothing

The natural way to run a timed problem is with a single deadline. You know you
have 35 minutes, you start, you go as fast as you can, and you find out how it
went when the interviewer says time is up

Watch that fail on a real problem. Take [Jump Game VI](https://leetcode.com/problems/jump-game-vi/),
where you stand at index 0, may jump forward up to `k` positions at a time, and
want the largest total of the values you land on. The recurrence is not hard to
see, since the best score at index `i` is `nums[i]` plus the best score among the
`k` positions you could have jumped from. The efficient version needs that
windowed maximum in `O(1)`, which is a
[monotonic deque](../../04_sliding_window/notes/04_window_max_min.md) sitting
inside a [one-dimensional DP](../../11_dp/notes/02_1d_dp.md)

So you chase it. You spend the first twenty-four minutes getting the deque
mechanics right in your head, start typing at minute 24, and hit the expiry
condition bug at minute 38, which is three minutes after the slot ended. You hand
in code that has never run

The recurrence itself was six lines of Python and would have taken five minutes.
The failure is not that you picked the wrong target. It is that the single
deadline gave you exactly **one measurement of your own progress, taken at the
end**, at the only moment when no decision is left to make. You were flying with
one instrument and it was the crash sensor

The repair follows immediately. If one reading at the end is useless, take
several readings during the run, at moments early enough that you can still act
on them. Split the box

## Splitting The Box Into Checkpoints

A **checkpoint** is a fixed minute paired with an artifact that must exist by
then, and an action to take if it does not. The minute alone is not a checkpoint,
because "I should be about halfway" is not something you can be wrong about
cleanly. "The brute force is stated out loud with its complexity" is

Here is the schedule for a 35-minute box. The sizes are not arbitrary, and the
reason each phase gets what it gets is in the last column

| By minute | What must exist                                                        | Why that much time                                                                                                                |
| --------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 3         | The contract restated in your words, and one small example walked      | Restating is two sentences and the example is one line, so anything past three minutes here is stalling rather than clarifying    |
| 8         | A correct brute force named out loud, with its complexity              | You are not coding it, only naming it, and if the simplest correct idea takes more than five minutes you have misread the problem |
| 14        | Either an optimization with a reason, or the decision to skip it       | Six minutes is one or two honest attempts at the bottleneck, which is enough to know whether the idea is there or not             |
| 27        | Code that runs, whichever approach you held at minute 14               | Thirteen minutes is a realistic medium, typed while narrating, which is slower than typing in silence                             |
| 32        | A hand trace on a small input, including the branch most likely wrong  | Five minutes is one trace done properly, and a trace you rush is a trace that confirms what you already believed                  |
| 35        | Time and space stated with named variables, plus the follow-up you see | Three minutes, because the analysis is a sentence each and you should have had both numbers in your head since minute 14          |

Scale the numbers, do not relearn them. A 60-minute loop with two problems runs
two boxes of about 25 minutes, so every checkpoint moves earlier by roughly a
third, and the commit checkpoint lands near minute 10

### The Commit Rule

Minute 14 is the only checkpoint that carries a hard rule, and it is the whole
reason the schedule exists:

> **Whatever approach you are holding at the commit checkpoint is the approach
> you code. Not the one you almost have**

An approach you "almost have" is worth zero, because the distance between almost
having an idea and having typed it correctly is exactly the distance you have no
evidence you can cover. The brute force is worth a great deal, because it is
correct, it demonstrates you understood the problem, and it gives the interviewer
something concrete to push against with a follow-up

Say the switch out loud when it happens, since an interviewer who sees you drop
to the slower approach silently reads it as giving up, while the same move
narrated reads as judgment:

> "I can see the bottleneck is recomputing the maximum over the last `k` entries,
> and I think a monotonic structure fixes it, but I do not have it clean yet. I
> am going to code the `O(n * k)` version now so we have something correct and
> running, and then optimize that inner `max` if there is time. The recurrence is
> identical either way, so the upgrade is one line"

That last sentence is doing real work. It tells the interviewer the slow version
is deliberately a **scaffold** rather than a retreat, and it commits you to an
upgrade that touches one expression rather than a rewrite

## Banking A Solution That Runs

The scaffold is only useful if the fast version is a local edit of it, so choose
the slow version that shares a shape with the fast one. For Jump Game VI that
means writing the recurrence as a real table and letting the windowed maximum be
the one slow piece

```python
def max_result_slow(nums: list[int], k: int) -> int:
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = nums[i] + max(dp[max(0, i - k) : i])
    return dp[-1]


assert max_result_slow([1, -1, -2, 4, -7, 3], 2) == 7
assert max_result_slow([10, -5, -2, 4, 0, 3], 3) == 17
assert max_result_slow([1, -5, -20, 4, -1, 3, -6, -3], 2) == 0
assert max_result_slow([5], 1) == 5
```

Six lines, correct, and it times out on large input, which is the ideal state to
be in at minute 20 rather than minute 35

**Why this particular slow version is the right scaffold**:

- The `dp` array, the base case, and the return are already final, so the
  optimization only has to replace `max(dp[max(0, i - k) : i])` with something that
  answers the same question faster
- `max(0, i - k)` guards the left edge, which is the
  [guarded reach-back](../../11_dp/notes/02_1d_dp.md) again. In this slice form
  the omission fails loudly rather than silently: since `k` never exceeds `n`, a
  bare `dp[i - k : i]` starts past `i` whenever `i < k` and comes back empty, so
  `max` raises `ValueError: max() iterable argument is empty` on the first index.
  Write the guard anyway, because the deque version below replaces that slice
  with a bare `dp[i - k]` lookup, where the same omission goes back to reading a
  real element from the far end and returning a wrong answer with no error
- The last assert is the single-element case, where the loop never runs and
  `dp[-1]` is the base case itself. That is the input an interviewer probes, and it
  costs one line to prove

Writing the asserts is part of the scaffold, not a luxury for later. Four
concrete cases take under a minute and convert "I think this is right" into "this
is right", which is the difference the minute-32 checkpoint is asking about

## Dry Run: A Clock That Slips

Here is what the schedule looks like on a run where the optimization does not
arrive in time. The interesting line is the rejected one

```text
min  0   problem read: "max total, jumping forward at most k"
min  2   contract restated, walked [1,-1,-2,4,-7,3] k=2 by hand -> 7      ON TIME
min  6   brute force named: try every jump sequence, exponential          ON TIME
min  8   improved to dp[i] = nums[i] + max(dp[i-k..i-1]), O(n*k)          ON TIME
min 12   bottleneck named: that inner max rescans k entries every step
min 14   COMMIT CHECKPOINT
         deque idea present but expiry condition still unclear
         REJECTED: keep chasing the O(n) version
         chosen: code the O(n*k) dp now, upgrade the max later
min 21   O(n*k) version runs, asserts pass
min 26   traced [5] k=1 and the all-negative case out loud
min 29   stated O(n*k) time, O(n) space, named the deque as the follow-up
min 33   with 6 minutes banked, swapped the max for the deque, reran asserts
```

The rejection at minute 14 is the entire technique. Nothing about the deque idea
got worse by being deferred, and the seven minutes spent coding the `O(n * k)`
version were not seven minutes lost, because the recurrence, the base case, the
edge guard, and the asserts are all shared with the fast version. The optimization
at minute 33 changed one expression on a body of code that was already correct

Compare that to the same clock without a commit checkpoint, where minutes 14
through 24 go into the deque, coding starts at 24, and minute 33 finds you
debugging expiry inside code that has never once run. Same idea, same candidate,
and no artifact at the end

The other thing to read off the trace is minute 29. Complexity got stated on the
slow version, before the upgrade existed. If the last four minutes had evaporated,
you would still have delivered a complete performance on a correct solution, which
is a good outcome. Save the analysis for after the optimization and a slipped
clock takes both

## Worked Example: [Jump Game VI](https://leetcode.com/problems/jump-game-vi/)

You start at index 0 of an integer array and want to reach the last index. From
index `i` you may jump to any index from `i + 1` through `i + k`, and your score
is the sum of the values at every index you land on, including the first and the
last. Return the largest score you can finish with

**Input**:

- `nums`, a `list[int]` holding at least one element, whose values may be
  negative, which is what stops "just take the biggest neighbour" from working
- `k`, an `int` that is at least 1 and never exceeds the length of `nums`, giving
  the furthest forward jump allowed in a single move
- Both the length of `nums` and `k` can be large enough that an `O(n * k)` scan is
  close to quadratic and times out, which is why the follow-up exists

**Output**: a single `int`, the maximum achievable sum over all legal jump
sequences from index 0 to the last index. It is not a count of jumps and not a
path, and it can be negative, since every route through an all-negative array
still has to land somewhere

The phrase that identifies the technique is "at most `k` positions forward",
because it makes the set of positions you could have arrived from a **window of
the last `k` table entries** rather than an arbitrary subset. Enumerating jump
sequences is exponential, since each position branches `k` ways. The DP fixes
that, and then `max` over the window is the remaining bottleneck, costing `k` per
index for `O(n * k)` overall

The window slides forward by exactly one position each step and you only ever ask
it for its maximum, which is the signal for a monotonic deque

> "The state is `dp[i]`, the best score for any route that ends standing on index
> `i`. Every route into `i` came from the previous `k` indices, so
> `dp[i] = nums[i] + max(dp[i-k..i-1])`. That inner `max` is a sliding-window
> maximum, so I will keep a deque of indices whose `dp` values decrease from the
> front, and read the answer off the front in `O(1)`"

Therefore,

1. Allocate `dp` with one slot per index and set `dp[0] = nums[0]`, because a
   route ending on index 0 has not jumped at all, so its score is that value alone
2. Keep a `deque` holding **indices**, not `dp` values, ordered so their `dp`
   values decrease from front to back. Storing indices is what lets you tell
   whether the best entry has fallen out of range, which a bare value cannot tell
   you
3. Seed the deque with index 0, since it is the only legal source for index 1 and
   the loop below assumes the deque is never empty when it reads the front
4. Walk `i` from 1 to the end. First drop indices that have aged out, meaning any
   front index below `i - k`, because a jump of more than `k` is not legal and the
   entry is now answering a question about a window you have already left
5. Read `dp[window[0]]` as the best reachable predecessor and set
   `dp[i] = nums[i] + dp[window[0]]`. The front is the maximum by construction, so
   this is `O(1)` rather than a scan
6. Before pushing `i`, pop every back entry whose `dp` value is at most `dp[i]`.
   Those entries are dominated, since `i` is both newer and at least as good,
   so any future window containing them contains `i` too and would never choose
   them
7. Append `i` and continue. Each index is pushed once and popped at most once, so
   the two inner `while` loops total `O(n)` work across the entire run rather than
   `O(k)` per step
8. Return `dp[-1]`, the best score for a route ending on the final index, which is
   the value the problem asks for

```python
from collections import deque


def max_result(nums: list[int], k: int) -> int:
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    window: deque[int] = deque([0])
    for i in range(1, n):
        while window[0] < i - k:
            window.popleft()
        dp[i] = nums[i] + dp[window[0]]
        while window and dp[window[-1]] <= dp[i]:
            window.pop()
        window.append(i)
    return dp[-1]


assert max_result([1, -1, -2, 4, -7, 3], 2) == 7
assert max_result([10, -5, -2, 4, 0, 3], 3) == 17
assert max_result([1, -5, -20, 4, -1, 3, -6, -3], 2) == 0
assert max_result([5], 1) == 5
```

Tracing `nums = [1, -1, -2, 4, -7, 3]` with `k = 2` shows both kinds of discard:

```text
i=0                        dp=[1,  _,  _, _,  _, _]   window=[0]
i=1  nums=-1  dp=-1+dp[0]  dp=[1,  0,  _, _,  _, _]   window=[0, 1]
i=2  nums=-2  dp=-2+dp[0]  dp=[1,  0, -1, _,  _, _]   window=[0, 1, 2]
i=3  nums= 4  EXPIRED 0    dp=[1,  0, -1, 4,  _, _]   window=[3]
              dominated: popped 2 then 1
i=4  nums=-7  dp=-7+dp[3]  dp=[1,  0, -1, 4, -3, _]   window=[3, 4]
i=5  nums= 3  dp= 3+dp[3]  dp=[1,  0, -1, 4, -3, 7]   window=[5]
              dominated: popped 4 then 3
```

Step `i=3` is the one to study. Index 0 held `dp = 1`, the largest value in the
table at that moment, and it was thrown away rather than used, because `i - k`
is `1` and a jump from index 0 to index 3 covers three positions when only two
are allowed. That is why the deque stores indices: the value 1 looks like the
right answer and is illegal, and only the index reveals it. `dp[3]` therefore came
out as `4 + dp[1]`, which is `4 + 0 = 4`, not `4 + 1 = 5`

The same step also discards indices 2 and 1 for the opposite reason. They are
still in range, but `dp[3] = 4` beats both and index 3 stays in the window longer
than either, so no future step could ever prefer them. Those entries are gone on
merit rather than on age

- **Time Complexity:** `O(n)`, where `n` is the length of `nums`, because the
  outer loop runs `n` times and each index enters and leaves the deque at most
  once, so both inner `while` loops sum to `O(n)` across the whole run rather than
  `O(k)` each
- **Space Complexity:** `O(n)` for the `dp` table plus `O(k)` for the deque, which
  is `O(n)` overall since `k` never exceeds `n`. The deque genuinely reaches its
  full `k + 1` entries on a strictly decreasing run of `dp` values, where nothing
  is ever dominated

## Time and Space Complexity

The row that matters here is the first one, because the point of a commit
checkpoint is that shipping it is a good outcome rather than a failure

| Approach                                                      | Time                                                                                                                               | Space                                                                                                          |
| ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| DP with `max` over the window, coded at the commit checkpoint | `O(n * k)`: `n` states, and each one rescans up to `k` earlier entries that the previous state already scanned                     | `O(n)`: the `dp` table only, since the slicing `max` allocates a temporary of size `k` that is freed each step |
| DP with a monotonic deque, the upgrade if the clock allows    | `O(n)`: `n` states, and every index is pushed and popped at most once, so the inner loops total `O(n)` rather than `O(k)` per step | `O(n)`: the `dp` table, plus `O(k)` for the deque when no entry is ever dominated, and `k <= n`                |
| Enumerating jump sequences, the brute force named at minute 8 | `O(k^n)`: every position branches up to `k` ways with no shared work between routes                                                | `O(n)`: recursion depth is one frame per position on the current route                                         |

The two DP rows have the same space class, which is worth saying out loud,
because it means the optimization is buying time at no cost in memory. That is a
rare and easy tradeoff to defend

## Summary

- A **time box** is a fixed budget for one phase of work with a stated action for
  when it expires. The action is the load-bearing half, since a budget you can
  overrun without consequence changes nothing about how you behave
  - Treat it as an invariant pointed at the clock rather than at your program
    state, checked at fixed moments during the run instead of once at the end
- Running a problem against a single deadline gives you exactly one reading of
  your own progress, taken at the moment when no decision remains. That is why a
  candidate can be twenty-four minutes into a 35-minute slot with a good idea and
  nothing typed
- Replace it with **checkpoints**, each being a minute paired with an artifact
  that has to exist by then. Roughly: contract by 3, brute force named by 8,
  optimization decided by 14, running code by 27, hand trace by 32, complexity by
  35, scaled proportionally for a shorter or longer slot
  - A checkpoint has to name an artifact, because "about halfway" is not a claim
    you can check, while "the brute force is stated with its complexity" is
- The **commit rule** at minute 14 says the approach you are holding is the one
  you code, and an approach you almost have counts as nothing. The distance
  between almost having an idea and having typed it correctly is exactly the
  distance you have no evidence you can cover
- Pick the slow version whose shape the fast version shares, so the upgrade is a
  local edit. In Jump Game VI the `O(n * k)` DP and the `O(n)` deque version differ
  only in how `max(dp[i-k..i-1])` is answered, so the table, the base case, the
  edge guard, and the asserts all carry over untouched
  - Say the switch out loud, because a silent drop to the slower approach reads as
    giving up while the same move narrated reads as judgment
- State complexity on whatever is currently running rather than saving it for the
  optimized version, since a clock that slips in the last five minutes then costs
  you the optimization only, instead of the optimization and the analysis together
- The most expensive habit is treating the brute force as something to skip once
  you are strong enough. It is the artifact that guarantees a scored performance,
  and it is also the thing whose repeated work names the bottleneck you are about
  to remove

## Interview Checklist

Before writing code, make sure you can answer each of these

```text
How many minutes of this slot are actually mine, once introductions are removed?
What are my checkpoint minutes for this slot, scaled from the 35-minute schedule?
Has the contract been restated and one example walked, or am I still stalling?
Is a correct brute force named out loud with its complexity, even unwritten?
At the commit checkpoint, do I hold a full approach or only most of one?
Which slow version shares its shape with the fast one, so the upgrade is one edit?
Did I say the drop to the slower approach out loud, and name the upgrade I see?
Is there code that runs and passes asserts, before I spend anything on speed?
Have I stated time and space on the version that currently exists?
If the clock died right now, what would the interviewer have actually seen?
```
