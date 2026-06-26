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
What pattern is this?
What state or invariant am I maintaining?
What is the base case or initialization?
When do I update the answer?
Why is the movement/transition valid?
What is the time and space complexity?
```
