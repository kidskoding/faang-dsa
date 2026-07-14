# Bitmask DP

## Pattern

Some problems ask you to visit every node, assign every worker, or cover every
skill exactly once, where the *order* of visiting/assigning matters for the
DP transition but the *set already handled* is the only state that matters
going forward. When N is small (typically N \<= 20), encode that set as an
integer bitmask and use it as a DP dimension: `dp[mask]` or `dp[mask][i]`.

## Intuition

Plain sequential DP (`11_dp`) indexes state by a position in a linear
structure — `dp[i]` means "the best answer using the first i elements." That
breaks down when the problem has no natural linear order and instead cares
about which *subset* of items has been used so far, in any order. Plain
subset enumeration (`15_bit_manipulation`) iterates over every subset once to
inspect or aggregate it — it never builds a DP table of subproblem answers
that other subsets transition into. Bitmask DP is the fusion: subsets become
the state space of a DP table, and transitions move from one mask to a larger
mask by adding one more element.

## How It Works

1. Pick what one bit represents (city visited, worker assigned, skill
   covered). N items means `1 << N` possible masks.
1. Define `dp[mask]` (or `dp[mask][i]` when you also need to track the last
   item touched, e.g. current city for a path) as the best/count/feasibility
   value achievable using exactly the items in `mask`.
1. Base case: the empty mask `dp[0]` (nothing chosen yet) or single-bit masks
   `dp[1 << i][i]` (just started at item i), seeded to a trivial value.
1. Transition: for each mask, try every bit `j` not yet set in `mask`. Move to
   `mask | (1 << j)` by "adding" item j, updating that state from the current
   one.
1. Answer sits at the full mask `dp[(1 << N) - 1]` (all items used), possibly
   minimized/maximized over the trailing index dimension.

## Template

```text
dp = 2D or 1D table indexed by mask (and optionally last index)
dp[base_mask] = base_value

for mask in range(1 << N):
    if dp[mask] is unset: continue
    for j in range(N):
        if mask & (1 << j): continue          # j already used
        new_mask = mask | (1 << j)
        dp[new_mask] = combine(dp[new_mask], dp[mask] + cost(mask, j))

return dp[(1 << N) - 1]
```

For path-style problems (must track *where* you are, not just *what* you've
used), add a second dimension for the current node/item:

```text
dp[mask][i] = best value ending at item i having used exactly the items in mask

dp[1 << i][i] = start_cost(i)  for every i

for mask in range(1 << N):
    for i in range(N):
        if dp[mask][i] is unset: continue
        for j in range(N):
            if mask & (1 << j): continue
            new_mask = mask | (1 << j)
            dp[new_mask][j] = combine(dp[new_mask][j], dp[mask][i] + edge(i, j))
```

## Complexity

```text
dp[mask] only:      Time O(2^N * N),   Space O(2^N)
dp[mask][i]:         Time O(2^N * N^2), Space O(2^N * N)
```

The `2^N` factor is why this pattern is reserved for small N — it stops being
tractable well before N reaches 25.

## Pitfalls

- Reaching for bitmask DP when N is large; if N > ~20, `2^N` states blow the
  time/space budget and a different pattern (greedy, flow, plain DP on a
  linear index) is needed instead.
- Confusing this with plain subset enumeration: if you are only generating or
  scanning every subset once with no table of subproblem answers feeding
  later subsets, that is `15_bit_manipulation`'s pattern, not this one.
- Forgetting the trailing "current item" dimension when the problem is
  path-like (order/adjacency matters between consecutive picks), leading to
  transitions that can't tell where the previous step ended.
- Iterating masks out of numeric order when the DP relies on `mask` always
  being built from smaller sub-masks — iterate `mask` from `0` upward (or
  recurse with memoization) so every dependency is already computed.
- Not initializing unreachable mask states to a sentinel (infinity / None) and
  then accidentally transitioning off a garbage value.

## Interview Checklist

Before coding, make sure you can answer:

```text
Is N small enough (roughly <= 20) that 2^N states are affordable?
Does the state I need to remember collapse to "which subset of items is
done," or do I also need to remember the last item touched?
Am I building dp[mask] from smaller sub-masks, not just scanning subsets
independently like 15_bit_manipulation's enumeration pattern?
What is the base case for the empty mask or each single-bit mask?
Is the final answer at the full mask (1 << N) - 1, possibly combined across
the trailing dimension?
```
