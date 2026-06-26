# DP Fundamentals

## Pattern

Dynamic programming solves problems with overlapping subproblems by storing answers to smaller states.

A DP solution has three parts:

1. State: what each `dp[...]` entry means.
2. Transition: how to compute a state from smaller states.
3. Order: the order in which states must be solved.

If you cannot say what the state means in one sentence, the solution is not ready to code.

## Intuition

DP is useful when brute force repeatedly solves the same smaller problem.

For example, in a recursive Fibonacci solution, `fib(5)` asks for `fib(4)` and `fib(3)`, and `fib(4)` also asks for `fib(3)`. That repeated `fib(3)` work is the overlap.

DP removes the repeated work by saving the result the first time it is computed.

## How It Works

Start by writing the brute force recurrence in words.

Then identify:

```text
state = the minimum information needed to describe a subproblem
transition = the choices or previous states that determine this state
base case = smallest known answers
answer = which state gives the final result
```

Common state shapes:

```text
dp[i] = best answer using items up to index i
dp[i][j] = best answer using prefixes i and j
dp[r][c] = best answer ending at grid cell r, c
dp[i][capacity] = best answer using first i items with capacity left
```

## Template: Top-Down Memoization

```text
def solve(state):
    if state is a base case:
        return base answer
    if state in memo:
        return memo[state]

    answer = combine recursive choices
    memo[state] = answer
    return answer
```

Use top-down when the recursive thinking is clearer.

## Template: Bottom-Up Tabulation

```text
initialize dp table with base cases

for state in valid order:
    dp[state] = transition from already-computed states

return final state
```

Use bottom-up when the dependency order is straightforward and recursion depth could be an issue.

## Example

For climbing stairs:

```text
dp[i] = number of ways to reach step i
```

To reach step `i`, you came from either `i - 1` or `i - 2`:

```text
dp[i] = dp[i - 1] + dp[i - 2]
```

Base cases:

```text
dp[0] = 1
dp[1] = 1
```

## Complexity

DP complexity comes from counting states and transition work.

```text
Time = number of states * work per transition
Space = number of stored states
```

Examples:

```text
1D DP over n positions: O(n) time, O(n) space
2D DP over n by m table: O(n*m) time, O(n*m) space
Knapsack over n items and capacity C: O(n*C) time
```

Space can often be optimized when each state only needs the previous one or two rows.

## Pitfalls

- Coding before defining the state.
- Choosing a state that does not contain enough information.
- Forgetting base cases.
- Filling the table in an order where dependencies are not ready.
- Optimizing space before the normal DP is correct.
- Using DP when the problem has no overlapping subproblems.

## Interview Checklist

Before coding, say these out loud:

```text
My state is ...
My base cases are ...
My transition is ...
The final answer is ...
There are ... states and each transition costs ...
```
