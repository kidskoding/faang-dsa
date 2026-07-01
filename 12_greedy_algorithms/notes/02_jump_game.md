# Jump Game Greedy

## Pattern

Track the farthest reachable index while scanning.

## Intuition

If the scan index ever passes the farthest reachable point, you are stuck.

## How It Works

You do not need to try all jumps; only the best reach matters.

## Template

```text
farthest = 0
for i in range(n):
    if i > farthest: return false
    farthest = max(farthest, i + nums[i])
return true
```

## Example

If index 3 is unreachable, no later index can be reached either.

## Complexity

```text
Time: O(n)
Space: O(1)
```

## Pitfalls

- Backtracking all jump paths unnecessarily.
- Updating reach after checking an unreachable index.
- Confusing Jump Game I with minimum jumps.

## Interview Checklist

Before coding, make sure you can answer:

```text
What single value am I tracking (farthest reachable index), and why is that enough?
Why does checking `i > farthest` before updating catch unreachability correctly?
Why is it safe to never backtrack to try a different jump length?
How does this differ from Jump Game II (minimum jumps), where I also need a level/boundary counter?
What happens at the last index — do I need `i > farthest` or `farthest >= n - 1` as the success condition?
```
