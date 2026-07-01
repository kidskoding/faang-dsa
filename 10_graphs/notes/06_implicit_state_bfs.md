# Implicit-State BFS

## Pattern

The graph is not given directly. Each state generates neighboring states by applying allowed moves.

## Intuition

Problems like locks, gene mutations, puzzles, and board games are shortest-path problems over states.

## How It Works

Treat each configuration as a node. Generate next configurations on the fly. BFS gives minimum moves.

## Template

```text
queue = deque([(start, 0)])
visited = {start}
while queue:
    state, dist = queue.popleft()
    if state == target:
        return dist
    for next_state in neighbors(state):
        if next_state not visited:
            visited.add(next_state)
            queue.append((next_state, dist + 1))
```

## Example

In open the lock, each wheel turn creates a neighboring lock state.

## Complexity

```text
Time: O(number of reachable states * transitions per state)
Space: O(number of reachable states)
```

## Pitfalls

- Not hashing state correctly.
- Forgetting dead states.
- Using DFS for shortest moves.

## Interview Checklist

Before coding, make sure you can answer:

```text
What does a "node" represent here (a lock combination, a word, a gene string), and how do I generate its neighbors on the fly?
How do I hash or represent a state so it can go into a visited set (tuple, string, frozenset)?
Are there dead/forbidden states that must be excluded before BFS even starts?
Why must this be BFS and not DFS, given the question asks for minimum number of moves/steps?
What is the branching factor per state, and how does that affect the state-space size in my complexity estimate?
```
